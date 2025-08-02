#!/usr/bin/env python3

import subprocess
import pyfiglet
import sys
import os

# === Optional: Terminal colors ===
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# === Clear screen (cross-platform) ===
os.system('cls' if os.name == 'nt' else 'clear')

# === Banner ===
ascii_banner = pyfiglet.figlet_format("IP Scanner")
print(f"{RED}{ascii_banner}{RESET}")
print(f"{YELLOW}🔍 Advanced Nmap Scanner - Powered by SnoopySugar 🦅\n{RESET}")

# === Get target info ===
ip = input(f"{CYAN}Enter target IP address: {RESET}")
port = input(f"{CYAN}Enter target port(s) (e.g., 80 or 1-1000 or 80,443): {RESET}")

# === Display scan options ===
print(f"""
{GREEN}Choose your scan flavor, sugarhead: 🍭
 1  = SYN Scan (-sS)
 2  = TCP Connect Scan (-sT)
 3  = UDP Scan (-sU)
 4  = ACK Scan (-sA)
 5  = FIN Scan (-sF)
 6  = Xmas Scan (-sX)
 7  = Null Scan (-sN)
 8  = Window Scan (-sW)
 9  = Maimon Scan (-sM)
10  = Protocol Scan (-sO)
11  = IP Protocol Scan (-sO)
12  = Ping Scan (-sn)
13  = OS Detection (-O)
14  = Aggressive Scan (-A)
15  = Version Detection Only (-sV)
16  = List Scan (-sL)
17  = Idle Scan (-sI){RESET}
""")

# === Get scan choice ===
try:
    scan = int(input(f"{CYAN}Enter option number: {RESET}"))
except ValueError:
    print(f"{RED}[-] Invalid input. Exiting.{RESET}")
    sys.exit(1)

output_file = "scan_output.txt"

# === Nmap Scan Flags Mapping ===
scan_commands = {
    1:  ["-sS"],
    2:  ["-sT"],
    3:  ["-sU"],
    4:  ["-sA"],
    5:  ["-sF"],
    6:  ["-sX"],
    7:  ["-sN"],
    8:  ["-sW"],
    9:  ["-sM"],
    10: ["-sO"],
    11: ["-sO"],
    12: ["-sn"],
    13: ["-O"],
    14: ["-A"],
    15: ["-sV"],
    16: ["-sL"],
    17: ["-sI", "zombie_host"],
}

# === Validate and prepare scan ===
if scan not in scan_commands:
    print(f"{RED}[-] Invalid scan type selected.{RESET}")
    sys.exit(1)

args = scan_commands[scan]
if "zombie_host" in args:
    zombie = input(f"{CYAN}Enter zombie host IP for Idle Scan: {RESET}")
    args = ["-sI", zombie]

# === Build and run Nmap command ===
nmap_command = ["nmap", ip, "-p", port] + args + ["-oN", output_file]

print(f"\n{YELLOW}[+] Running: {' '.join(nmap_command)}{RESET}\n")
subprocess.run(nmap_command)
print(f"\n{GREEN}[+] Scan complete. Output saved to {output_file}{RESET}")
