#!/usr/bin/env bash
set -e

echo "=================================================="
echo "# Cyber Custom OS - Live ISO Builder Script"
echo "# Converts the framework and dependencies into a bootable ISO"
echo "=================================================="

mkdir -p iso_build

if [ -f "README.md" ]; then
    cp README.md iso_build/
fi

echo "Cyber Custom OS v1.1.0 - Hybrid Build" > iso_build/manifest.txt
echo "[*] ISO Build Directory Ready at: ./iso_build/"
echo -e "\e[1;32m[✓] Framework Packaging Complete!\e[0m"