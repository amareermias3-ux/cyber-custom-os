import os
import sys

# Windows ወይም Linux መሆኑን መፈተሽ
IS_WINDOWS = os.name == 'nt'
SUDO_PREFIX = "" if IS_WINDOWS else "sudo "

def show_banner():
    os.system('cls' if IS_WINDOWS else 'clear')
    print("=" * 55)
    print("      CYBER CUSTOM OS - CONTROL CENTER")
    print("      [ Kali + Parrot + Tails + Qubes Hybrid ]")
    print("=" * 55)

def main_menu():
    while True:
        show_banner()
        print("\n1. 🔒 Privacy Mode አብራ (Tails Tor Redirection)")
        print("2. 🔓 Privacy Mode አጥፋ (Normal Network)")
        print("3. 🌐 የ IP እና የ Tor ሁኔታን ፈትሽ")
        print("4. 🛠️   Security Tools Container አስነሳ (Kali/CAINE)")
        print("5. 🚪 ውጣ (Exit)")
        print("-" * 55)
        
        choice = input("ምርጫዎን ያስገቡ (1-5): ").strip()
        
        if choice == '1':
            print("\n[+] Privacy Mode በመጀመር ላይ...")
            if IS_WINDOWS:
                print("⚠️ ማሳሰቢያ፡ የTor iptables መደለያ በሙሉ አቅሙ የሚሰራው በLinux/WSL አካባቢ ላይ ነው።")
            os.system(f"{SUDO_PREFIX}bash ./privacy/anon_mode.sh start")
            input("\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '2':
            print("\n[-] Privacy Mode በማቆም ላይ...")
            os.system(f"{SUDO_PREFIX}bash ./privacy/anon_mode.sh stop")
            input("\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '3':
            print("\n[*] የኔትወርክ ሁኔታ በማረጋገጥ ላይ...")
            if IS_WINDOWS:
                # Windows ላይ ያለ sudo curl መጠቀም
                os.system("curl https://check.torproject.org/api/ip")
            else:
                os.system(f"{SUDO_PREFIX}bash ./privacy/anon_mode.sh status")
            input("\n\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '4':
            print("\n[+] Security Container በመክፈት ላይ...")
            os.system("docker run -it cyber-tools:v1")
            input("\nለመቀጠል Enter ን ይጫኑ...")
        elif choice == '5':
            print("\nስለተጠቀሙ እናመሰግናለን! መልካም ቀን።")
            sys.exit(0)
        else:
            input("\n❌ የተሳሳተ ምርጫ! እባክዎን ከ 1 እስከ 5 ይመረጡ (Enter ይጫኑ)...")

if __name__ == "__main__":
    main_menu()