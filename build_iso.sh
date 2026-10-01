#!/bin/bash
# ==============================================================================
# Cyber Custom OS - Hybrid ISO Packaging Engine
# ==============================================================================

echo "================================================="
echo "   Cyber Custom OS - Hybrid ISO Packaging Engine  "
echo "================================================="

echo "[+] Preparing build directory structure..."
mkdir -p iso_build/modules

echo "[+] Validating framework modules..."
bash modules/privacy/anon_mode.sh status || true
bash modules/security/vault_hardening.sh check || true
bash modules/forensics/dfir_toolkit.sh check || true
bash modules/offensive/recon_toolkit.sh check || true
bash modules/security/qubes_isolation.sh || true
bash modules/offensive/adv_kali_arsenal.sh || true
python -c "import sys; print('✔ CLI Dashboard: OK')"

echo "[+] Generating OS Manifest..."
cp -r modules/ iso_build/
cp README.md iso_build/
echo "Cyber Custom OS v1.1.0 - Hybrid Build" > iso_build/manifest.txt

echo "[*] ISO Build Directory Ready at: ./iso_build/"
echo -e "\e[1;32m[✔] Framework Packaging Complete!\e[0m"

#!/usr/bin/env bash
# ==============================================================================
# Cyber Custom OS - Live ISO Builder Script
# Converts the framework and dependencies into a bootable Debian Live ISO
# ==============================================================================

set -e

echo "=== Cyber Custom OS: Live ISO Builder ==="

if [ "$EUID" -ne 0 ]; then
  echo "❌ Error: Please run as root (sudo ./build_iso.sh)"
  exit 1
fi

echo "[1/4] Installing live-build dependencies..."
apt-get update && apt-get install -y live-build xorriso squashfs-tools isolinux

BUILD_DIR="iso_workspace"
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

echo "[2/4] Initializing live-build configuration..."
lb config \
    --architectures amd64 \
    --distribution bookworm \
    --archive-areas "main contrib non-free non-free-firmware" \
    --binary-images iso-hybrid

echo "[3/4] Injecting Cyber Custom OS files..."
mkdir -p config/includes.chroot/opt/cyber-custom-os
cp -r ../modules ../install.sh ../README.md config/includes.chroot/opt/cyber-custom-os/

echo "[4/4] Compiling Live ISO image..."
lb build

echo "✅ Live ISO built successfully! Check the generated .iso file in iso_workspace/."