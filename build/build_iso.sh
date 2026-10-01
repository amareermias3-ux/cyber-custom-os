#!/bin/bash

# ==========================================
# Cyber Custom OS - Master ISO Builder Script
# Automated Build Process using Debian Live-Build
# ==========================================

echo "[+] የ Cyber Custom OS ግንባታ በሂደት ላይ ነው..."

# 1. አስፈላጊ መሳሪያዎች መጫናቸውን ማረጋገጥ
sudo apt-get update
sudo apt-get install -y live-build docker.io git

# 2. የ Docker Image ግንባታ (Kali + CAINE Tools)
echo "[+] የ Docker Containers ግንባታ ተጀምሯል..."
docker build -t cyber-tools:v1 -f ../modules/containers/sec_tools.Dockerfile .

# 3. የ Live-Build ስራ ቦታ ማዘጋጀት
BUILD_DIR="iso_workspace"
mkdir -p $BUILD_DIR && cd $BUILD_DIR

# 4. የ Debian Live-Build ውቅር (Configuration)
lb config \
   --debian-installer live \
   --architectures amd64 \
   --distribution bookworm \
   --archive-areas "main contrib non-free non-free-firmware" \
   --interactive shell

# 5. የPrivacy ስክሪፕት (Tails mode) ወደ ሲስተሙ ማስገባት
mkdir -p config/includes.chroot/usr/local/bin/
cp ../../modules/privacy/anon_mode.sh config/includes.chroot/usr/local/bin/anon-mode
chmod +x config/includes.chroot/usr/local/bin/anon-mode

# 6. የመጨረሻውን Bootable ISO መገንባት
echo "[+] ISO ምስሉ እየተመረተ ነው (ይህ ጥቂት ደቂቃዎችን ሊወስድ ይችላል)..."
sudo lb build

echo "[+] ግንባታው በስኬት ተጠናቋል! ISO ፋይሉ በ iso_workspace ፎልደር ውስጥ ይገኛል።"