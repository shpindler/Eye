import socket
from typing import List, Tuple


def scan_ports(ip: str, port_range: Tuple[int, int]) -> List[int]:
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        if not sock.connect_ex((ip, port)):
            open_ports.append(port)
            sock.close()

    return open_ports


if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Replace with the target IP address
    port_range = (1, 1024)  # Define the port range to scan

    print(f"Scanning IP: {target_ip}...")
    open_ports = scan_ports(target_ip, port_range)
    print(f"Open ports: {open_ports}")
