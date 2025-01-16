# Recon

## Subdomains

```
subfinder -d example.com -all > subfinder.txt
assetfinder -subs-only example.com > assetfinder.txt
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u > crtsh.txt
cat *.txt | sort -u > all_subs.txt
```
