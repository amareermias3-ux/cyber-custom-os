# Cyber Custom OS - Hybrid Security Framework

የተለያዩ ታዋቂ የሳይበር ሴኪዩሪቲ ኦፐሬቲንግ ሲስተሞችን (**Kali Linux**, **Parrot OS**, **Tails OS**, **Qubes OS** እና **CAINE**) አበይት ባህሪያት በማጣመር የተሰራ Custom Hybrid Security Framework ነው።

## 🚀 ዋና ዋና ባህሪያት (Key Modules)

1. **🔒 Tails Privacy Mode (`modules/privacy/anon_mode.sh`):**
   - የኢንተርኔት ትራፊክን በሙሉ በ Tor Network በኩል አዙሮ የመምራትና ማንነትን የመሰወር አቅም።
2. **🛡️ Parrot Kernel Hardening (`modules/security/vault_hardening.sh`):**
   - የስርዓቱን ሴኪዩሪቲ (Anti-Exploit, Kernel Network Parameters) የማጠናከር ስራ ይሰራል::
3. **🧹 Anti-Forensics RAM Wipe (`modules/security/vault_hardening.sh`):**
   - የ RAM Cache እና የቴምፖራሪ ፋይሎችን በአስተማማኝ ሁኔታ ማጽዳት::
4. **🔍 CAINE Digital Forensics Toolkit (`modules/forensics/dfir_toolkit.sh`):**
   - የ Volatile Evidence ሰብስቦ መመርመር እና የፋይሎችን Integrity በ SHA-256 ማረጋገጥ::
5. **🎯 Kali Recon & Vulnerability Audit (`modules/offensive/recon_toolkit.sh`):**
   - አውቶሜትድ የዒላማ መረጃ ሰብሳቢና የፖርት/ኤችቲቲፒ ሄደር መፈተሻ::
6. **💻 Control Center CLI Dashboard (`modules/dashboard.py`):**
   - ሁሉንም ሞጁሎች በአንድ ማዕከላዊ ትእዛዝ መቆጣጠሪያ ማቀናጀት::

## 🛠️ አጠቃቀም (Usage)

የቁጥጥር ማዕከሉን (Dashboard) ለማስነሳት፡

```bash
python modules/dashboard.py