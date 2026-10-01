#!/bin/bash
# Cyber Custom OS - Kali Inspired Automated Recon Engine

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}[+] Running Cyber Custom OS - Kali Recon Engine...${NC}"

# 1. Target Connectivity & HTTP Header Audit
quick_recon() {
    read -p "የዒላማውን (Target) IP ወይም Domain ያስገቡ: " target
    if [ -z "$target" ]; then
        echo -e "${RED}[!] እባክዎን ትክክለኛ IP ወይም Domain ያስገቡ!${NC}"
        return
    fi
    echo -e "\n${GREEN}[*] Target Availability check ($target)...${NC}"
    echo "-----------------------------------------"
    ping -c 3 "$target" 2>/dev/null || ping -n 3 "$target" 2>/dev/null
    echo "-----------------------------------------"
    echo -e "${GREEN}[*] Fetching Target Web Server Headers...${NC}"
    curl -I -s -L "https://$target" 2>/dev/null || curl -I -s -L "http://$target" 2>/dev/null
    echo "-----------------------------------------"
    echo -e "${GREEN}[✔] Recon Scan Completed.${NC}"
}

case "$1" in
    scan)
        quick_recon
        ;;
    *)
        echo "Usage: $0 {scan}"
        exit 1
esac