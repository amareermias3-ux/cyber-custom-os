#!/usr/bin/env bash
# Cyber Custom OS - Automated Setup & Environment Installer Script

set -e

GREEN="\033[92m"
CYAN="\033[96m"
YELLOW="\033[93m"
RED="\033[91m"
RESET="\033[0m"

echo -e "${CYAN}====================================================${RESET}"
echo -e "${GREEN}    🛡️  CYBER CUSTOM OS - AUTOMATED SETUP SCRIPT  🛡️️${RESET}"
echo -e "${CYAN}====================================================${RESET}"

echo -e "\n${YELLOW}[1/4] Checking Python environment...${RESET}"
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}[✓] Python3 is installed.${RESET}"
else
    echo -e "${RED}[X] Python3 is missing! Please install Python 3.${RESET}"
    exit 1
fi

echo -e "\n${YELLOW}[2/4] Installing Python dependencies (psutil)...${RESET}"
python3 -m pip install --upgrade pip --quiet || true
python3 -m pip install psutil --quiet && echo -e "${GREEN}[✓] psutil library installed successfully.${RESET}"

echo -e "\n${YELLOW}[3/4] Configuring execution permissions...${RESET}"
chmod +x build_iso.sh modules/dashboard.py 2>/dev/null || true
echo -e "${GREEN}[✓] Permissions updated for core scripts.${RESET}"

echo -e "\n${YELLOW}[4/4] Checking system security packages (Nmap, Net-tools)...${RESET}"
if command -v apt-get &>/dev/null; then
    read -p "Do you want to install core system tools (nmap, net-tools)? [y/N]: " choice
    case "$choice" in 
      y|Y ) 
        echo -e "${GREEN}[*] Updating package lists and installing tools...${RESET}"
        sudo apt-get update && sudo apt-get install -y nmap net-tools
        ;;
      * ) 
        echo -e "${YELLOW}[!] Skipping system package installation.${RESET}"
        ;;
    esac
else
    echo -e "${YELLOW}[!] Non-Debian/APT environment detected. Skipping package manager installation.${RESET}"
fi

echo -e "\n${CYAN}====================================================${RESET}"
echo -e "${GREEN}    ✅ Cyber Custom OS Setup Completed Successfully!  ${RESET}"
echo -e "${CYAN}====================================================${RESET}"

read -p "Would you like to launch the CLI Dashboard now? [y/N]: " run_dash
case "$run_dash" in 
  y|Y ) 
    python3 modules/dashboard.py
    ;;
  * ) 
    echo -e "${GREEN}Setup finished. You can run dashboard anytime with: python3 modules/dashboard.py${RESET}"
    ;;
esac