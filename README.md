# recon

Initial recon steps on a given host.

## Running
```
pip3 install -r requirements.txt
python3 recon.py host=example.com     

     !!!           |"|                     #   ___          _   _     
  `  _ _  '       _|_|_         ,,,,,      #  <_*_>        '\-//`    
 -  (OXO)  -      (o o)        /(o o)\     #  (o o)         (o o)     
ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo--8---(_)--Ooo-ooO--(_)--Ooo-


Recon init on <example.com>
ip found: 44.225.41.25
Looking for open ports...

Open ports and services on 44.225.41.25:
# Port 80: http
# Port 443: http
# Port 3389: ms-wbt-server

whois example.com ?


registrar: redacted
whois_server: redacted
referral_url: redacted
updated_date: redacted
creation_date: redacted
expiration_date: redacted
name_servers: redacted
emails: redacted
dnssec: redacted
name: redacted
org: redacted
address: redacted
city: redacted
state: redacted
registrant_postal_code: redacted
country: redacted
```

## TODO

See `shell/recon.sh`
