#!/usr/bin/env bash
# ==============================================================================
# Cyber Custom OS - Automated Test Suite
# ==============================================================================

echo "[+] Starting Automated Module Tests..."

# 1. Test Python Dashboard Syntax
echo "[*] Testing Python Dashboard syntax..."
python -m py_compile modules/dashboard.py
if [ $? -eq 0 ]; then
    echo "  [✓] dashboard.py: PASS"
else
    echo "  [✗] dashboard.py: FAIL"
    exit 1
fi

# 2. Test Shell Scripts Syntax
SCRIPTS=(
    "modules/privacy/anon_mode.sh"
    "modules/security/vault_hardening.sh"
    "modules/forensics/dfir_toolkit.sh"
    "modules/offensive/recon_toolkit.sh"
    "modules/security/qubes_isolation.sh"
    "modules/offensive/adv_kali_arsenal.sh"
    "install.sh"
)

for script in "${SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        bash -n "$script"
        if [ $? -eq 0 ]; then
            echo "  [✓] $script: PASS"
        else
            echo "  [✗] $script: FAIL"
            exit 1
        fi
    else
        echo "  [!] File $script not found!"
    fi
done

echo "[+] All Module Tests Passed Successfully!"