#!/usr/bin/env bash
set -e

echo "Running Automated Unit Tests..."

# Test 1: Check Python syntax
python3 -m py_compile modules/dashboard.py
echo "[✓] Python Dashboard syntax check passed."

# Test 2: Check bash scripts
bash -n build_iso.sh
bash -n install.sh
echo "[✓] Shell scripts syntax check passed."

echo "All tests completed successfully!"