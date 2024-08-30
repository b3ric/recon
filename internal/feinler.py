import whois
from datetime import datetime

def feinler(host):
    who = whois.whois(host)
    for k, v in who.items():
        if isinstance(v, list):
            v = [item.strftime('%Y-%m-%d %H:%M:%S') if isinstance(item, datetime) else item for item in v]
        elif isinstance(v, datetime):
            v = v.strftime('%Y-%m-%d %H:%M:%S')
        if k != 'status' and k != 'domain_name':
            print(f"{k}: {v}")
