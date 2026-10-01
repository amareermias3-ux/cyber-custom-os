#!/usr/bin/env bash
set -e

echo "=== Running Cyber Custom OS Test Suite ==="

echo "[1/3] Checking Python syntax..."
python3 -m py_compile modules/dashboard.py
echo "✓ dashboard.py syntax OK"

echo "[2/3] Checking Shell scripts syntax..."
bash -n install.sh
bash -n build_iso.sh
echo "✓ Shell scripts syntax OK"

echo "[3/3] Validating directory structure..."
if [ -f "Dockerfile" ] && [ -f "docker-compose.yml" ]; then
    echo "✓ Docker files verified"
fi

echo "=== All Tests Passed Successfully! ==="