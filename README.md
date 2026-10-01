# 🛡️ Cyber Custom OS - Hybrid Security Framework

ይህ ፕሮጀክት የተለያዩ ታዋቂ የሳይበር ሴኪዩሪቲ ኦፕሬቲንግ ሲስተሞችን (Kali, Parrot OS, Tails, Qubes OS እና CAINE) አሪፍ አሪፍ ባህሪያት በማዋሀድ የተዘጋጀ ብጁ (Custom) የደህንነት ማዕቀፍ ነው።

## 🚀 ዋና ዋና ባህሪያት (Features)

* **Tails Privacy Engine (`anon_mode.sh`):** ሁሉንም የሲስተሙን TCP/DNS የኢንተርኔት እንቅስቃሴዎች በTor አውታረ መረብ በኩል በማሳለፍ ማንነትን ይደብቃል።
* **Qubes-Inspired Isolation (`sec_tools.Dockerfile`):** የKali እና CAINE መሳሪያዎችን በDocker Container ውስጥ ነጥሎ በማስኬድ የዋናውን ሲስተም ደህንነት ይጠብቃል።
* **CAINE Forensics Tools:** የውሂብ ማገገሚያ እና የዲጂታል ፎረንሲክስ ምርመራ መሳሪያዎችን ያካትታል።
* **BackBox-Style Live ISO Builder (`build_iso.sh`):** በDebian Live-Build አማካኝነት ሙሉ በሙሉ የሚነሳ Bootable ISO ያመርታል።
* **CLI Control Dashboard (`dashboard.py`):** ሁሉንም ሞጁሎች በቴርሚናል ላይ በቀላሉ የሚያስተዳድር የቁጥጥር ሰሌዳ።

## 📁 የፕሮጀክቱ ማውጫ (Directory Structure)

```text
cyber-custom-os/
├── build/
│   └── build_iso.sh          # ISO ምስሉን የሚገነባ ዋና ስክሪፕት
├── modules/
│   ├── dashboard.py          # የCLI መቆጣጠሪያ ሰሌዳ
│   ├── privacy/
│   │   └── anon_mode.sh      # የTor ትራፊክ መደለያ ስክሪፕት
│   └── containers/
│       └── sec_tools.Dockerfile # የKali እና CAINE መሳሪያዎች Dockerfile
└── README.md