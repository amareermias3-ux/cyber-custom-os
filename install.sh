#!/bin/bash
# ==============================================================================
# Cyber Custom OS - Automated System Installer
# ==============================================================================

echo "================================================="
echo "   Installing Cyber Custom OS Framework          "
echo "================================================="

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "[-] Error: Please run as root (sudo ./install.sh)"
  exit 1
fi

echo "[+] Updating system packages..."
apt-get update -y && apt-get install -y python3 git curl firejail apparmor

echo "[+] Setting executable permissions for modules..."
chmod +x build_iso.sh
chmod +x modules/privacy/*.sh
chmod +x modules/security/*.sh
chmod +x modules/forensics/*.sh
chmod +x modules/offensive/*.sh

echo "[+] Creating global executable symlink..."
ln -sf $(pwd)/modules/dashboard.py /usr/local/bin/cyber-os

echo "================================================="
echo "[✔] Installation Complete!"
echo "[*] Launch dashboard anytime using command: cyber-os"
echo "================================================="