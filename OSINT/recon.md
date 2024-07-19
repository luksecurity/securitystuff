# Recon

## Subdomains

```
subfinder -d <domain> -o subfinder.txt
sublist3r -d <domain> -o sublister.txt
cat subfinder.txt sublister.txt >> subs.txt
rm subfinder.txt sublister.txt
httpx -l subs.txt -threads 200 -o alive.txt
cat alive.txt | gau --subs --blacklist png,jpg,jpeg,svg | tee -a endpoints.txt
```
