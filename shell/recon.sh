# TODO: Decide what should be implemented from here in Python
subfinder -d "$target" --silent -o "$HOME/$folder_name/subdomains_subfinder.txt"
assetfinder --subs-only "$target" | tee "$HOME/$folder_name/subdomains_assetfinder.txt"
amass enum -d "$target" -brute | tee "$HOME/$folder_name/subdomains_amass.txt"
crt.sh/crt.sh -d "$target" | sort | uniq |  grep -Eo --color=auto "(^|[^a-zA-Z0-9_.-])([a-zA-Z0-9_-]+\.)?${target}" | tee "$HOME/$folder_name/subdomains_crt-sh.txt"
knockpy "$target" | tee "$HOME/bb/$folder_name/subdomains_knockpy.txt"
cat "$HOME/$folder_name/subdomains_subfinder.txt" "$HOME/$folder_name/subdomains_assetfinder.txt" "$HOME/$folder_name/subdomains_crt-sh.txt" | sort -u >> "$HOME/$folder_name/all_subdomains.txt"
cat "$HOME/$folder_name/all_subdomains.txt" | httpx -sc -cl -silent | tee "$HOME/$folder_name/httpx.txt"
echo "Subdomain Enumeration is complete" | notify -silent