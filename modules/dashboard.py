#!/usr/bin/env python3
import os
import sys
import time
import socket
import psutil

# ANSI Color Codes for Terminal UI
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def get_ip():
    """Gets the primary local IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def draw_bar(percent, length=20):
    """Draws a visual progress bar for resource usage."""
    filled = int(length * percent / 100)
    bar = "█" * filled + "-" * (length - filled)
    if percent > 85:
        color = RED
    elif percent > 60:
        color = YELLOW
    else:
        color = GREEN
    return f"[{color}{bar}{RESET}] {percent:.1f}%"

def display_dashboard():
    """Clears terminal and prints the main dashboard interface."""
    os.system("clear" if os.name == "posix" else "cls")
    hostname = socket.gethostname()
    ip_addr = get_ip()

    cpu_usage = psutil.cpu_percent(interval=0.3)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print(f"{CYAN}{BOLD}" + "="*58 + f"{RESET}")
    print(f"{GREEN}{BOLD}          🛡️  CYBER CUSTOM OS - CLI DASHBOARD  🛡️{RESET}")
    print(f"{CYAN}{BOLD}" + "="*58 + f"{RESET}")
    print(f"{BOLD} Hostname :{RESET} {hostname:<20} | {BOLD}Local IP:{RESET} {ip_addr}")
    print(f"{CYAN}" + "-"*58 + f"{RESET}")

    print(f"\n{BOLD}📊 System Resource Monitor:{RESET}")
    print(f" CPU Usage : {draw_bar(cpu_usage)}")
    print(f" RAM Usage : {draw_bar(mem.percent)} ({mem.used // (1024**2)}MB / {mem.total // (1024**2)}MB)")
    print(f" Disk Space: {draw_bar(disk.percent)} ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)")

    print(f"\n{CYAN}" + "-"*58 + f"{RESET}")
    print(f"{BOLD}🛠️  Quick Security Tools Menu:{RESET}")
    print(" [1] Check Nmap Scanner Status")
    print(" [2] View Active Network Connections")
    print(" [3] Run System Update Check")
    print(" [4] Refresh Dashboard")
    print(" [0] Exit Dashboard")
    print(f"{CYAN}" + "="*58 + f"{RESET}")

def main():
    while True:
        display_dashboard()
        choice = input(f"\n{YELLOW}{BOLD}Select an option [0-4]: {RESET}").strip()
        
        if choice == "1":
            print(f"\n{GREEN}[*] Checking Nmap Status...{RESET}")
            os.system("nmap --version 2>/dev/null || echo 'Nmap is not installed. Install via: sudo apt install nmap'")
            input("\nPress Enter to return...")
        elif choice == "2":
            print(f"\n{GREEN}[*] Listening Ports & Active Connections:{RESET}")
            os.system("ss -tuln 2>/dev/null || netstat -tuln")
            input("\nPress Enter to return...")
        elif choice == "3":
            print(f"\n{GREEN}[*] System Package Update Check...{RESET}")
            os.system("sudo apt update -s 2>/dev/null || echo 'Note: Run with sudo for full update permissions'")
            input("\nPress Enter to return...")
        elif choice == "4":
            continue
        elif choice == "0":
            print(f"\n{GREEN}Exiting Dashboard. Goodbye!{RESET}")
            sys.exit(0)
        else:
            print(f"\n{RED}Invalid selection! Please enter a number between 0 and 4.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()