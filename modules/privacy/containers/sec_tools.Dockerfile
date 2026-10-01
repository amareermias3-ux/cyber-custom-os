# ==========================================
# Cyber Custom OS - Containerized Toolset
# Combines Kali Pentesting & CAINE Forensics
# ==========================================

FROM kalilinux/kali-rolling

# በኢንስታሌሽን ወቅት ጥያቄ እንዳይጠይቅ ለማድረግ
ENV DEBIAN_FRONTEND=noninteractive

# የሲስተም ፓኬጆችን ማዘመን እና ዋና ዋና መሳሪያዎችን መጫን
RUN apt-get update && apt-get install -y \
    nmap \
    metasploit-framework \
    tshark \
    john \
    sleuthkit \
    autopsy \
    sqlmap \
    nikto \
    curl \
    wget \
    net-tools \
    iputils-ping \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# መስሪያ ቦታ ማዘጋጀት
WORKDIR /workspace

# ሲከፈት በይነገጽ (Bash Terminal) እንዲያዘጋጅ
CMD ["/bin/bash"]