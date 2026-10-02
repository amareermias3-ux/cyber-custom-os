import os
import sys
import time

# እያንዳንዱን ሞጁል ለየብቻ Import ማድረግ (አንዱ ቢጠፋ ሌላኛው እንዳይበላሽ)
try:
    import modules.network_scanner as network_scanner
except ImportError:
    pass

try:
    import modules.logger as logger
except ImportError:
    pass

try:
    import modules.tool_manager as tool_manager
except ImportError:
    pass

try:
    import modules.privacy_mode as privacy_mode
except ImportError:
    pass

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    print("="*55)
    print(" 🛡️  CYBER CUSTOM OS - ENTERPRISE DASHBOARD v3.0 🛡")
    print("="*55)

def main_menu():
    while True:
        clear_screen()
        show_banner()
        print("[1] Show System Information")
        print("[2] Check Network Status")
        print("[3] Run System Update (apt update)")
        print("[4] Web Dashboard Instruction")
        print("[5] Run Security Port Scanner (Nmap Style)")
        print("[6] Generate System Audit Log (RAM/CPU)")
        print("[7] OS Tool & Advanced Package Manager")
        print("[8] Activate Privacy & Anonymity Mode (Tails Style)")
        print("[0] Exit / Shutdown")
        print("="*55)
        
        choice = input("Select an option [0-8]: ")
        
        if choice == '1':
            print("\n[+] Displaying System Information...")
            os.system("uname -a" if os.name == 'posix' else "systeminfo | findstr /B /C:\"OS Name\" /C:\"OS Version\"")
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            print("\n[+] Checking Network Status...")
            os.system("ifconfig" if os.name == 'posix' else "ipconfig")
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            print("\n[+] Running System Update...")
            os.system("apt update && apt upgrade -y" if os.name == 'posix' else "echo '[-] Unsupported on Windows'")
            input("\nPress Enter to continue...")
            
        elif choice == '4':
            print("\n[+] The Real-Time Web Dashboard runs on Flask.")
            print("[+] Open a new terminal and run: python3 app.py")
            print("[+] Then open http://127.0.0.1:5000 in your browser.")
            input("\nPress Enter to continue...")
            
        elif choice == '5':
            print("\n[+] Initializing Security Port Scanner...")
            try:
                target = input("Enter target IP or Hostname (e.g., 127.0.0.1): ") or "127.0.0.1"
                network_scanner.run_port_scan(target)
            except NameError:
                print("[-] network_scanner module not loaded.")
            input("\nPress Enter to continue...")
            
        elif choice == '6':
            print("\n[+] Generating System Audit Log...")
            try:
                metrics = logger.log_system_metrics()
                print(f"[+] Successfully Logged: {metrics}")
            except NameError:
                print("[-] logger module not loaded.")
            input("\nPress Enter to continue...")
            
        elif choice == '7':
            try:
                tool_manager.run_manager()
            except NameError:
                print("[-] tool_manager module not loaded.")
            input("\nPress Enter to continue...")
            
        elif choice == '8':
            try:
                privacy_mode.enable_privacy_mode()
            except NameError:
                print("[-] privacy_mode module not loaded.")
            input("\nPress Enter to continue...")
            
        elif choice == '0':
            print("\n[+] Shutting down Cyber Custom OS Dashboard. Goodbye!")
            sys.exit(0)
            
        else:
            print("\n[-] Invalid selection. Please choose a number between 0 and 8.")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()