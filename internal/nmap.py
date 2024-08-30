import nmap
from typing import Dict


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