import socket
import concurrent.futures
import time

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port
    except Exception:
        pass
    return None

def run_port_scan(target_host, ports_to_scan=range(1, 1025)):
    print(f"\n[+] Starting Security Port Scan on target: {target_host}")
    start_time = time.time()
    open_ports = []
    
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"[+] Resolved IP: {target_ip}")
    except socket.gaierror:
        print("[-] Error: Hostname could not be resolved.")
        return []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in ports_to_scan}
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)

    open_ports.sort()
    duration = round(time.time() - start_time, 2)
    print(f"[+] Scan completed in {duration} seconds.")
    print(f"[+] Found {len(open_ports)} open port(s): {open_ports}\n")
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP or Hostname (e.g., 127.0.0.1 or scanme.nmap.org): ") or "127.0.0.1"
    run_port_scan(target)