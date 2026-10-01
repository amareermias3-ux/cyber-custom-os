#!/bin/bash

# ==========================================
# Cyber Custom OS - Anonymity Routing Module
# (Tails-inspired Tor Traffic Redirection)
# ==========================================

TOR_USER="debian-tor"
TRANS_PORT="9040"
DNS_PORT="5353"

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "[-] እባክዎን ስክሪፕቱን በ Sudo/Root ያስኬዱ! (ምሳሌ: sudo ./anon_mode.sh start)"
  exit 1
fi

start_anon() {
    echo "[+] Anon Mode እየተበራ ነው... (Tor Routing)"
    
    # 1. የ Tor አገልግሎትን ማስጀመር
    systemctl start tor || service tor start
    
    # 2. የቆዩ IPtables Rules ማፅዳት
    iptables -F
    iptables -t nat -F

    # 3. የ DNS ጥያቄዎችን በሙሉ ወደ Tor ማዞር (DNS Leak ለመከላከል)
    echo "nameserver 127.0.0.1" > /etc/resolv.conf

    # 4. ሁሉንም TCP ትራፊክ ወደ Tor TransPort ማዞር
    iptables -t nat -A OUTPUT -p tcp -m owner --uid-owner $TOR_USER -j ACCEPT
    iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports $DNS_PORT
    iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports $TRANS_PORT

    echo "[+] Anon Mode በትክክል ሰርቷል! አሁን አጠቃላይ የኔትወርክ ትራፊክዎ በ Tor በኩል ያልፋል።"
}

stop_anon() {
    echo "[-] Anon Mode እየጠፋ ነው... (Normal Network)"
    
    # IPtables ደንቦችን ማፅዳት
    iptables -F
    iptables -t nat -F

    # DNS ወደ መደበኛ መመለስ
    echo "nameserver 8.8.8.8" > /etc/resolv.conf

    echo "[+] የሲስተሙ የኔትወርክ መስመር ወደ መደበኛ ሁኔታ ተመልሷል።"
}

status_anon() {
    echo "[*] የክፍለ-ጊዜውን (IP) አድራሻ እና የ Tor ሁኔታ በመፈተሽ ላይ..."
    curl -s https://check.torproject.org/api/ip
}

case "$1" in
    start)
        start_anon
        ;;
    stop)
        stop_anon
        ;;
    status)
        status_anon
        ;;
    *)
        echo "አጠቃቀም: sudo $0 {start|stop|status}"
        exit 1
esac