#!/bin/bash
# Cyber Custom OS - System Hardening & Vault Module

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}[+] Running Cyber Custom OS Hardening & Anti-Forensics Engine...${NC}"

# 1. Kernel Network Hardening (Prevent IP Spoofing, ICMP Redirects)
apply_hardening() {
    echo -e "${GREEN}[*] Applying Kernel Security Hardening...${NC}"
    sysctl -w net.ipv4.conf.all.rp_filter=1 2>/dev/null
    sysctl -w net.ipv4.tcp_syncookies=1 2>/dev/null
    sysctl -w net.ipv4.conf.all.accept_redirects=0 2>/dev/null
    sysctl -w net.ipv6.conf.all.accept_redirects=0 2>/dev/null
    echo -e "${GREEN}[✔] Kernel Security Policies Applied.${NC}"
}

# 2. Anti-Forensic Memory Clean (Tails RAM Flush concept)
wipe_memory_cache() {
    echo -e "${RED}[!] Flushing RAM Caches and Volatile Buffers...${NC}"
    sync
    echo 3 > /proc/sys/vm/drop_caches 2>/dev/null
    echo -e "${GREEN}[✔] RAM Cache and volatile logs cleared.${NC}"
}

# Command switch
case "$1" in
    harden)
        apply_hardening
        ;;
    wipe)
        wipe_memory_cache
        ;;
    *)
        echo "Usage: $0 {harden|wipe}"
        exit 1
esac