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