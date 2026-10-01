#!/bin/bash
# Cyber Custom OS - CAINE Inspired Forensics & DFIR Toolkit

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}[+] Running Cyber Custom OS - CAINE Forensics Module...${NC}"

# 1. System Incident Response Audit
incident_audit() {
    echo -e "${GREEN}[*] Collecting Volatile System Artifacts...${NC}"
    echo "-----------------------------------------"
    echo " [1] Active Network Connections"
    echo "-----------------------------------------"
    netstat -an 2>/dev/null || tasklist /svc 2>/dev/null
    echo -e "\n${GREEN}[✔] Volatile evidence snapshot taken.${NC}"
}

# 2. Evidence Integrity Check (SHA-256 Hash)
file_hash() {
    read -p "የሚመረመረውን ፋይል Path ያስገቡ: " filepath
    if [ -f "$filepath" ]; then
        echo -e "${GREEN}[*] Computing SHA-256 Hash for Evidence Integrity...${NC}"
        certutil -hashfile "$filepath" SHA256 2>/dev/null || sha256sum "$filepath"
    else
        echo -e "${RED}[!] ፋይሉ አልተገኘም! እባክዎን የፋይሉን ትክክለኛ አድራሻ ያረጋግጡ።${NC}"
    fi
}

case "$1" in
    audit)
        incident_audit
        ;;
    hash)
        file_hash
        ;;
    *)
        echo "Usage: $0 {audit|hash}"
        exit 1
esac