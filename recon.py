import socket
import nmap
import sys
import argparse

def find_open_ports(ip: str) -> dict[int, str]:
    nm = nmap.PortScanner()
    
    try:
        nm.scan(ip, arguments='-sV')
    except nmap.PortScannerError as e:
        print(f"nmap error occurred: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

    open_ports = {}

    for proto in nm[ip].all_protocols():
        ports = nm[ip][proto].keys()
        for port in ports:
            service_name = nm[ip][proto][port]['name']
            open_ports[port] = service_name

    return open_ports

def main(): 
    parser = argparse.ArgumentParser(description="Port scanner using nmap")
    parser.add_argument("host", help="Host to scan (domain or IP address)")
    args = parser.parse_args()

    host = args.host

    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror as e:
        print(f"DNS resolution error: {e}")
        sys.exit(1)
    
    open_ports = find_open_ports(ip)

    if open_ports:
        print(f"Open ports and services on {ip}:")
        for port, service in open_ports.items():
            print(f"Port {port}: {service}")
    else:
        print(f"No open ports found on {ip} or nmap scan failed.")

if __name__ == "__main__":
    main()
