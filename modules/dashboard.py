import os
import sys

IS_WINDOWS = os.name == 'nt'
SUDO_PREFIX = "" if IS_WINDOWS else "sudo "

# Multilingual Translations Dictionary
LANG = {
    'EN': {
        'title': "CYBER CUSTOM OS - CONTROL CENTER",
        'subtitle': "[ Kali + Parrot + Tails + Qubes + CAINE Hybrid ]",
        'opt1': "🔒 Enable Privacy Mode (Tails Tor Redirection)",
        'opt2': "🔓 Disable Privacy Mode (Normal Network)",
        'opt3': "🌐 Check IP & Tor Connection Status",
        'opt4': "🛡️ Apply Kernel Hardening (Parrot Anti-Exploit)",
        'opt5': "🧹 Anti-Forensic RAM Wipe (Tails Memory Clean)",
        'opt6': "🔍 CAINE Digital Forensics & Incident Audit",
        'opt7': "🔑 Evidence Integrity Checker (SHA-256 Hash)",
        'opt8': "🎯 Kali Recon & Vulnerability Audit Engine",
        'opt9': "🛠️ Security Tools Container (Kali/CAINE Sandbox)",
        'opt10': "🌐 Switch Language / ቋንቋ ይቀይሩ (Current: English)",
        'opt11': "🚪 Exit",
        'prompt': "Enter your choice (1-11): ",
        'start_privacy': "\n[+] Starting Privacy Mode...",
        'stop_privacy': "\n[-] Stopping Privacy Mode...",
        'check_ip': "\n[*] Checking Network & Tor Status...",
        'apply_hardening': "\n[+] Applying Kernel & Network Hardening...",
        'ram_wipe': "\n[!] Flushing RAM Cache & Volatile Logs...",
        'forensics_audit': "\n[+] Running Incident Audit...",
        'integrity_check': "\n[+] Verifying Evidence Integrity...",
        'kali_recon': "\n[+] Starting Kali Target Reconnaissance Engine...",
        'sec_container': "\n[+] Launching Security Container...",
        'press_enter': "\nPress Enter to continue...",
        'invalid_opt': "\n❌ Invalid choice! Please select 1-11 (Press Enter)...",
        'exit_msg': "\nThank you for using Cyber Custom OS! Goodbye."
    },
    'AM': {
        'title': "CYBER CUSTOM OS - የመቆጣጠሪያ ማዕከል",
        'subtitle': "[ Kali + Parrot + Tails + Qubes + CAINE Hybrid ]",
        'opt1': "🔒 Privacy Mode አብራ (Tails Tor Redirection)",
        'opt2': "🔓 Privacy Mode አጥፋ (Normal Network)",
        'opt3': "🌐 የ IP እና የ Tor ሁኔታን ፈትሽ",
        'opt4': "🛡️ Kernel Hardening ተግብር (Parrot Anti-Exploit)",
        'opt5': "🧹 Anti-Forensic RAM Wipe (Tails Memory Clean)",
        'opt6': "🔍 CAINE Digital Forensics & Incident Audit",
        'opt7': "🔑 Evidence Integrity Checker (SHA-256 Hash)",
        'opt8': "🎯 Kali Recon & Vulnerability Audit Engine",
        'opt9': "🛠️ Security Tools Container (Kali/CAINE Sandbox)",
        'opt10': "🌐 Switch Language / ቋንቋ ይቀይሩ (አሁን፡ አማርኛ)",
        'opt11': "🚪 ውጣ (Exit)",
        'prompt': "ምርጫዎን ያስገቡ (1-11): ",
        'start_privacy': "\n[+] Privacy Mode በመጀመር ላይ...",
        'stop_privacy': "\n[-] Privacy Mode በማቆም ላይ...",
        'check_ip': "\n[*] የኔትወርክ ሁኔታ በማረጋገጥ ላይ...",
        'apply_hardening': "\n[+] Kernel & Network Hardening በመተግበር ላይ...",
        'ram_wipe': "\n[!] RAM Cache & Volatile Log Flush በማድረግ ላይ...",
        'forensics_audit': "\n[+] Incident Audit በማካሄድ ላይ...",
        'integrity_check': "\n[+] Evidence Integrity Verification...",
        'kali_recon': "\n[+] Kali Target Reconnaissance Engine በመጀመር ላይ...",
        'sec_container': "\n[+] Security Container በመክፈት ላይ...",
        'press_enter': "\nለመቀጠል Enter ን ይጫኑ...",
        'invalid_opt': "\n❌ የተሳሳተ ምርጫ! እባክዎን ከ 1 እስከ 11 ይመረጡ (Enter ይጫኑ)...",
        'exit_msg': "\nስለተጠቀሙ እናመሰግናለን! መልካም ቀን።"
    }
}

current_lang = 'EN'  # Default Language

def show_banner():
    os.system('cls' if IS_WINDOWS else 'clear')
    txt = LANG[current_lang]
    print("=" * 68)
    print(f"      {txt['title']}")
    print(f"      {txt['subtitle']}")
    print("=" * 68)

def main_menu():
    global current_lang
    while True:
        show_banner()
        txt = LANG[current_lang]
        print(f"\n1.  {txt['opt1']}")
        print(f"2.  {txt['opt2']}")
        print(f"3.  {txt['opt3']}")
        print(f"4.  {txt['opt4']}")
        print(f"5.  {txt['opt5']}")
        print(f"6.  {txt['opt6']}")
        print(f"7.  {txt['opt7']}")
        print(f"8.  {txt['opt8']}")
        print(f"9.  {txt['opt9']}")
        print(f"10. {txt['opt10']}")
        print(f"11. {txt['opt11']}")
        print("-" * 68)
        
        choice = input(txt['prompt']).strip()
        
        if choice == '1':
            print(txt['start_privacy'])
            os.system(f"{SUDO_PREFIX}bash ./modules/privacy/anon_mode.sh start")
            input(txt['press_enter'])
        elif choice == '2':
            print(txt['stop_privacy'])
            os.system(f"{SUDO_PREFIX}bash ./modules/privacy/anon_mode.sh stop")
            input(txt['press_enter'])
        elif choice == '3':
            print(txt['check_ip'])
            if IS_WINDOWS:
                os.system("curl https://check.torproject.org/api/ip")
            else:
                os.system(f"{SUDO_PREFIX}bash ./modules/privacy/anon_mode.sh status")
            input(txt['press_enter'])
        elif choice == '4':
            print(txt['apply_hardening'])
            os.system(f"{SUDO_PREFIX}bash ./modules/security/vault_hardening.sh harden")
            input(txt['press_enter'])
        elif choice == '5':
            print(txt['ram_wipe'])
            os.system(f"{SUDO_PREFIX}bash ./modules/security/vault_hardening.sh wipe")
            input(txt['press_enter'])
        elif choice == '6':
            print(txt['forensics_audit'])
            os.system("bash ./modules/forensics/dfir_toolkit.sh audit")
            input(txt['press_enter'])
        elif choice == '7':
            print(txt['integrity_check'])
            os.system("bash ./modules/forensics/dfir_toolkit.sh hash")
            input(txt['press_enter'])
        elif choice == '8':
            print(txt['kali_recon'])
            os.system("bash ./modules/offensive/recon_toolkit.sh scan")
            input(txt['press_enter'])
        elif choice == '9':
            print(txt['sec_container'])
            os.system("docker run -it cyber-tools:v1")
            input(txt['press_enter'])
        elif choice == '10':
            current_lang = 'AM' if current_lang == 'EN' else 'EN'
        elif choice == '11':
            print(txt['exit_msg'])
            sys.exit(0)
        else:
            input(txt['invalid_opt'])

if __name__ == "__main__":
    main_menu()