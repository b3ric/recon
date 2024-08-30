import socket
from time import sleep
import sys
import argparse
from internal import feinler, nmap

def recon(host):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror as e:
        print(f"DNS resolution error: {e}")
        sys.exit(1)
    
    sleep(1/2)
    print(f'ip found: {ip}\nLooking for open ports...')
    
    open_ports = nmap.find_open_ports(ip)

    if open_ports:
        print(f"\nOpen ports and services on {ip}:")
        for port, service in open_ports.items():
            print(f"# Port {port}: {service}")
    else:
        print(f"No open ports found on {ip} or nmap scan failed.")
    
    print(f"\nwhois {host} ?\n\n")
    feinler.feinler(host)

if __name__ == "__main__":
    ascii_art = """
     !!!           |"|                     #   ___          _   _     
  `  _ _  '       _|_|_         ,,,,,      #  <_*_>        '\\-//`    
 -  (OXO)  -      (o o)        /(o o)\     #  (o o)         (o o)     
ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo--8---(_)--Ooo-ooO--(_)--Ooo-
"""
    print(ascii_art + "\n")
    sleep(1/2)

    parser = argparse.ArgumentParser(description="Port scanner using nmap")
    parser.add_argument("host", help="Host to scan (domain or IP address)")
    args = parser.parse_args()

    host = args.host.split("=")[1]
    print(f'Recon init on <{host}>')
    recon(host)
