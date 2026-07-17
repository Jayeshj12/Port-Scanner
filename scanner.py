import socket
import os
from datetime import datetime

COMMON_PORTS = [
    20, 21, 22, 23, 25,
    53, 80, 110, 139,
    143, 443, 445,
    3306, 3389
]

SERVICE_NAMES = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)

print("=" * 40)
print("        PORT SCANNER")
print("=" * 40)

target = input("Enter IP address: ")

print(f"\nScanning {target}...\n")

report = []

report.append("=" * 40)
report.append("PORT SCANNER REPORT")
report.append("=" * 40)
report.append(f"Target : {target}")
report.append(f"Scan Time : {datetime.now()}")
report.append("")

open_ports = []

for port in COMMON_PORTS:

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:

            service = SERVICE_NAMES.get(port, "Unknown")

            print(f"✅ Port {port} ({service}) is OPEN")

            report.append(f"[OPEN]   {port} ({service})")

            open_ports.append(port)

        else:

            print(f"❌ Port {port} is CLOSED")

            report.append(f"[CLOSED] {port}")

        sock.close()

    except Exception as e:

        print(f"Error scanning port {port}: {e}")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

filename = f"{REPORT_FOLDER}/scan_{timestamp}.txt"

with open(filename, "w") as file:
    file.write("\n".join(report))

print("\n===================================")
print("Scan Completed")
print(f"Report saved to:\n{filename}")
print("===================================")