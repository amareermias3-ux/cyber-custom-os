#!/bin/bash
# Cyber Custom OS - Automated Live ISO Builder Script

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}====================================================${NC}"
echo -e "${BLUE}   Cyber Custom OS - Hybrid ISO Packaging Engine    ${NC}"
echo -e "${BLUE}====================================================${NC}"

BUILD_DIR="iso_build"

echo -e "${GREEN}[+] Preparing build directory structure...${NC}"
mkdir -p "$BUILD_DIR/modules"
cp -r modules/* "$BUILD_DIR/modules/"
cp README.md "$BUILD_DIR/" 2>/dev/null

echo -e "${GREEN}[+] Validating framework modules...${NC}"
[ -f "$BUILD_DIR/modules/privacy/anon_mode.sh" ] && echo "  ✔ Privacy Module: OK"
[ -f "$BUILD_DIR/modules/security/vault_hardening.sh" ] && echo "  ✔ Security Module: OK"
[ -f "$BUILD_DIR/modules/forensics/dfir_toolkit.sh" ] && echo "  ✔ Forensics Module: OK"
[ -f "$BUILD_DIR/modules/offensive/recon_toolkit.sh" ] && echo "  ✔ Recon Module: OK"
[ -f "$BUILD_DIR/modules/dashboard.py" ] && echo "  ✔ CLI Dashboard: OK"

echo -e "${GREEN}[+] Generating OS Manifest...${NC}"
echo "Cyber Custom OS v1.0 - Hybrid Security Framework" > "$BUILD_DIR/manifest.txt"
date >> "$BUILD_DIR/manifest.txt"

echo -e "${BLUE}[*] ISO Build Directory Ready at: ./$BUILD_DIR/${NC}"
echo -e "${GREEN}[✔] Framework Packaging Complete!${NC}"