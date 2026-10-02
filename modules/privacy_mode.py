import os
import subprocess

def enable_privacy_mode():
    print("\n[+] Activating Tails-Style Privacy Mode...")
    print("[+] Starting Tor Service...")
    
    try:
        # Tor አገልግሎትን መጀመር
        subprocess.run(["service", "tor", "start"], check=True)
        print("[+] Tor service is running.")
        
        # የ Proxychains ማረጋገጫ (IP አድራሻ መቀየሩን ማረጋገጥ)
        print("[+] Verifying anonymous IP via Proxychains...")
        result = subprocess.run(["proxychains4", "curl", "-s", "https://ifconfig.me"], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"[+] Success! Your anonymous IP is: {result.stdout.strip()}")
        else:
            print("[-] Could not verify anonymous IP. Ensure Tor and Proxychains are installed.")
            
    except Exception as e:
        print(f"[-] Error activating privacy mode: {e}")
        print("[*] Hint: Use the Tool Manager [Option 7] -> [Category 3] to install Tor and Proxychains first.")

if __name__ == "__main__":
    enable_privacy_mode()