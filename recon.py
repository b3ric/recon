import socket
from time import sleep
import nmap
import sys
import argparse
from typing import Dict
from internal import ident

def find_open_ports(ip: str) -> Dict[int, str]:
    nm = nmap.PortScanner()
    
    try:
        nm.scan(ip, arguments='-sVC')
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
    ident.test()
    parser = argparse.ArgumentParser(description="Port scanner using nmap")
    parser.add_argument("host", help="Host to scan (domain or IP address)")
    args = parser.parse_args()

    host = args.host.split("=")[1]

    print(f'Recon init on <{host}>')
    
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
    ascii_art = """
     !!!           |"|                     #   ___          _   _     
  `  _ _  '       _|_|_         ,,,,,      #  <_*_>        '\\-//`    
 -  (OXO)  -      (o o)        /(o o)\     #  (o o)         (o o)     
ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo--8---(_)--Ooo-ooO--(_)--Ooo-
"""
    print(ascii_art + "\n")
    sleep(1)

    main()
