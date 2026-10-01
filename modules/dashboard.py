import os
import sys

IS_WINDOWS = os.name == 'nt'
SUDO_PREFIX = "" if IS_WINDOWS else "sudo "

def show_banner():
    os.system('cls' if IS_WINDOWS else 'clear')
    print("=" * 60)
    print("      CYBER CUSTOM OS - CONTROL CENTER")
    print("      [ Kali + Parrot + Tails + Qubes + CAINE Hybrid ]")
    print("=" * 60)

def main_menu():
    while True:
        show_banner()
        print("\n1. 🔒 Privacy Mode አብራ (Tails Tor Redirection)")
        print("2. 🔓 Privacy Mode አጥፋ (Normal Network)")
        print("3. 🌐 የ IP እና የ Tor ሁኔታን ፈትሽ")
        print("4. 🛡️  Kernel Hardening ተግብር (Parrot Anti-Exploit)")
        print("5. 🧹 Anti-Forensic RAM Wipe (Tails Memory Clean)")
        print("6. 🛠️   Security Tools Container (Kali/CAINE Sandbox)")
        print("7. 🚪 ውጣ (Exit)")
        print("-" * 60)
        
        choice = input("ምርጫዎን ያስገቡ (1-7): ").strip()
        
        if choice == '1':
            print("\n[+] Privacy Mode በመጀመር ላይ...")
            os.system(f"{SUDO_PREFIX}bash ./modules/privacy/anon_mode.sh start")
            input("\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '2':
            print("\n[-] Privacy Mode በማቆም ላይ...")
            os.system(f"{SUDO_PREFIX}bash ./modules/privacy/anon_mode.sh stop")
            input("\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '3':
            print("\n[*] የኔትወርክ ሁኔታ በማረጋገጥ ላይ...")
            if IS_WINDOWS:
                os.system("curl https://check.torproject.org/api/ip")
            else:
                os.system(f"{SUDO_PREFIX}bash ./modules/privacy/anon_mode.sh status")
            input("\n\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '4':
            print("\n[+] Kernel & Network Hardening በመተግበር ላይ...")
            os.system(f"{SUDO_PREFIX}bash ./modules/security/vault_hardening.sh harden")
            input("\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '5':
            print("\n[!] RAM Cache & Volatile Log Flush በማድረግ ላይ...")
            os.system(f"{SUDO_PREFIX}bash ./modules/security/vault_hardening.sh wipe")
            input("\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '6':
            print("\n[+] Security Container በመክፈት ላይ...")
            os.system("docker run -it cyber-tools:v1")
            input("\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '7':
            print("\nስለተጠቀሙ እናመሰግናለን! መልካም ቀን።")
            sys.exit(0)
        else:
            input("\n❌ የተሳሳተ ምርጫ! እባክዎን ከ 1 እስከ 7 ይመረጡ (Enter ይጫኑ)...")

if __name__ == "__main__":
    main_menu()