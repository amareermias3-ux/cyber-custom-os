## 📥 Quick Installation (One-Command Setup)

Run the following command in your Linux terminal to automatically install Cyber Custom OS:

```bash
curl -sSL [https://raw.githubusercontent.com/amareermias3-ux/cyber-custom-os/main/install.sh](https://raw.githubusercontent.com/amareermias3-ux/cyber-custom-os/main/install.sh) | sudo bash

# Cyber Custom OS - Hybrid Security Framework 🛡️🌍

![CI/CD Build Status](https://github.com/amareermias3-ux/cyber-custom-os/actions/workflows/ci.yml/badge.svg)

A custom hybrid security framework combining features from top cybersecurity Linux distributions: **Kali Linux**, **Parrot OS**, **Tails OS**, **Qubes OS**, **CAINE OS**, and **BlackArch**.

---

## 🇬🇧 English Documentation

### 🚀 Key Modules
1. **🔒 Tails Privacy Mode (`modules/privacy/anon_mode.sh`):** Redirects system traffic through Tor network.
2. **🛡️ Parrot Kernel Hardening (`modules/security/vault_hardening.sh`):** Anti-exploit and kernel security enhancements.
3. **🧹 Anti-Forensics RAM Wipe (`modules/security/vault_hardening.sh`):** Flushes RAM cache and temporary volatile logs.
4. **🔍 CAINE Digital Forensics Toolkit (`modules/forensics/dfir_toolkit.sh`):** Collects volatile evidence and computes SHA-256 integrity hashes.
5. **🎯 Kali Recon Engine (`modules/offensive/recon_toolkit.sh`):** Automated target reconnaissance and HTTP header audit.
6. **🧊 Qubes-Style App Isolation (`modules/security/qubes_isolation.sh`):** AppArmor and Firejail sandboxing.
7. **⚔️ BlackArch Offensive Arsenal (`modules/offensive/adv_kali_arsenal.sh`):** Penetration testing tools and exploit wrappers.
8. **💻 Multilingual Control Center (`modules/dashboard.py`):** Interactive CLI supporting English & Amharic switching.

### 🛠️ Quick Usage
Launch Central Control Dashboard:
```bash
python modules/dashboard.py