# Cyber Custom OS - Hybrid Security Framework 🛡️🌍

A custom hybrid security framework combining features from top cybersecurity Linux distributions: **Kali Linux**, **Parrot OS**, **Tails OS**, **Qubes OS**, and **CAINE OS**.

---

## 🇬🇧 English Documentation

### 🚀 Key Modules
1. **🔒 Tails Privacy Mode (`modules/privacy/anon_mode.sh`):** Redirects system traffic through Tor network for anonymous browsing.
2. **🛡️ Parrot Kernel Hardening (`modules/security/vault_hardening.sh`):** Implements anti-exploit and kernel security enhancements.
3. **🧹 Anti-Forensics RAM Wipe (`modules/security/vault_hardening.sh`):** Flushes RAM cache and temporary volatile logs.
4. **🔍 CAINE Digital Forensics Toolkit (`modules/forensics/dfir_toolkit.sh`):** Collects volatile evidence and computes SHA-256 integrity hashes.
5. **🎯 Kali Recon Engine (`modules/offensive/recon_toolkit.sh`):** Automated target reconnaissance and HTTP header audit.
6. **💻 Control Center Dashboard (`modules/dashboard.py`):** Interactive CLI supporting dynamic Language Switching (English / Amharic).

### 🛠️ Quick Usage
Launch Central Control Dashboard:
```bash
python modules/dashboard.py