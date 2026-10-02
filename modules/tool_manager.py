import os
import subprocess

TOOLS_CATEGORIES = {
    "1": {"name": "Information Gathering", "tools": ["nmap", "whois", "dnsutils"]},
    "2": {"name": "Vulnerability Analysis", "tools": ["nikto", "sqlmap"]},
    "3": {"name": "Privacy & Anonymity (Tails Style)", "tools": ["tor", "proxychains4"]},
    "4": {"name": "Bug Bounty & HTB (Athena Style)", "tools": ["openvpn", "curl", "wget"]}
}

def install_tools(tools_list):
    print(f"\n[+] Installing tools: {', '.join(tools_list)}")
    try:
        # Update package list first
        subprocess.run(["apt", "update"], check=True)
        # Install selected tools
        subprocess.run(["apt", "install", "-y"] + tools_list, check=True)
        print("[+] Installation completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error installing packages: {e}")

def run_manager():
    while True:
        print("\n" + "="*40)
        print(" 🛠️️  CYBER OS - ADVANCED TOOL MANAGER 🛠️")
        print("="*40)
        for key, value in TOOLS_CATEGORIES.items():
            print(f"[{key}] {value['name']}")
        print("[0] Return to Main Menu")
        print("="*40)
        
        choice = input("Select a category to install tools [0-4]: ")
        
        if choice == '0':
            break
        elif choice in TOOLS_CATEGORIES:
            selected_tools = TOOLS_CATEGORIES[choice]["tools"]
            install_tools(selected_tools)
        else:
            print("[-] Invalid selection.")

if __name__ == "__main__":
    run_manager()