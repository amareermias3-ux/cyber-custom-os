import os
import subprocess
import time

def connect_htb_vpn():
    print("\n[+] Hack The Box / OpenVPN Connector")
    ovpn_file = input("Enter path to your .ovpn configuration file (e.g., lab_user.ovpn): ").strip()
    
    if not os.path.exists(ovpn_file):
        print(f"[-] File '{ovpn_file}' not found! Please check the path and try again.")
        return

    print(f"[+] Connecting to OpenVPN using {ovpn_file}...")
    try:
        # OpenVPN በ Background ማስነሳት
        subprocess.Popen(["openvpn", "--config", ovpn_file])
        print("[+] OpenVPN connection initialized in background.")
        time.sleep(3)
        
        # Connection ማረጋገጥ (tun0 interface መኖሩን ማየት)
        res = subprocess.run(["ip", "addr", "show", "tun0"], capture_output=True, text=True)
        if "tun0" in res.stdout:
            print("[+] Successfully connected to HTB Lab Network (tun0 interface active)!")
        else:
            print("[*] OpenVPN is running. Verify connection using 'ifconfig' or 'ip a'.")
    except Exception as e:
        print(f"[-] Error connecting to OpenVPN: {e}")

def auto_recon_target():
    print("\n[+] Automated Bug Bounty Target Reconnaissance")
    target = input("Enter Target IP or Domain (e.g., 10.10.10.X or example.com): ").strip()
    
    if not target:
        print("[-] Target cannot be empty.")
        return

    print(f"\n[+] Running Automated Reconnaissance on {target}...")
    
    # 1. Quick Port Scan
    print("\n--- Phase 1: Port Scanning ---")
    subprocess.run(["nmap", "-F", target])
    
    # 2. HTTP/HTTPS Header Check
    print("\n--- Phase 2: Web Target Inspection ---")
    try:
        subprocess.run(["curl", "-I", "-s", f"http://{target}"], timeout=5)
    except Exception:
        print("[-] Could not retrieve HTTP headers.")

def run_bugbounty_menu():
    while True:
        print("\n" + "="*45)
        print(" 🎯 CYBER OS - ATHENA STYLE BUG BOUNTY HUB 🎯")
        print("="*45)
        print("[1] Connect to HTB / TryHackMe VPN (.ovpn)")
        print("[2] Run Automated Target Reconnaissance")
        print("[0] Return to Main Menu")
        print("="*45)
        
        choice = input("Select an option [0-2]: ").strip()
        
        if choice == '1':
            connect_htb_vpn()
        elif choice == '2':
            auto_recon_target()
        elif choice == '0':
            break
        else:
            print("[-] Invalid option.")

if __name__ == "__main__":
    run_bugbounty_menu()