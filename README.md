# 🛡️ Cyber Custom OS Framework

![Release](https://img.shields.io/badge/release-v1.2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![Docker](https://img.shields.io/badge/docker-ready-0db7ed.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**Cyber Custom OS** is a hybrid cybersecurity, privacy, and system-hardening framework combining key features inspired by **Kali Linux, Parrot OS, Tails, Qubes OS, CAINE, and BlackArch**.

---

## 🌟 Core Features

- 📊 **Real-Time System Dashboard:** Live monitoring of CPU, RAM, OS kernel, and IP addresses via Python CLI.
- 🕵️ **Anonymity Suite (Tails Mode):** MAC address spoofing, Tor routing, and RAM/cache cleanup scripts.
- 🔒 **System Isolation (Qubes Mode):** Sandboxed environment setup and security vault hardening.
- 🧪 **Automated Testing:** Built-in shell script & python syntax validator (`tests/test_modules.sh`).
- 🐳 **Dockerized Deployment:** Containerized setup via `Dockerfile` & `docker-compose.yml`.
- 💿 **Live ISO Generator:** Custom Debian-based ISO compilation script (`build_iso.sh`).

---

## 🚀 Quick Start Guide

### 1️⃣ Run Locally (Linux / Windows Git Bash)
```bash
# Clone repository
git clone [https://github.com/amareermias3-ux/cyber-custom-os.git](https://github.com/amareermias3-ux/cyber-custom-os.git)
cd cyber-custom-os

# Run test suite
bash tests/test_modules.sh

# Launch Dashboard
python modules/dashboard.py