#!/usr/bin/env python3
import socket
import sys

VERSION = "1.0"
USAGE = f"""ident-user-enum v{VERSION}

Usage: ident-user-enum.py ip port [ port [ port ... ] ]

Queries the ident service (113/TCP) to determine the OS-level user running 
the process listening on a given TCP port. More than one port can be supplied.\n\n"""


def test():
    print("hellooooooooo")

def lookup_ident(ip, port, timeout=5):
    try:
        sock = socket.create_connection((ip, port), timeout=timeout)
        sock.send(f"{port}, 113\r\n".encode('utf-8'))
        response = sock.recv(1024).decode('utf-8').strip()
        sock.close()

        if response:
            return response.split(':')[-1].strip()
        else:
            return "<unknown>"
    except Exception:
        return "<unknown>"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(USAGE)

    ip = sys.argv[1]
    ports = sys.argv[2:]

    print(f"ident-user-enum v{VERSION}\n\n")

    for port in ports:
        username = lookup_ident(ip, int(port))
        print(f"{ip}:{port}\t{username}")
