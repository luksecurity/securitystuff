# 🕵️‍♂️ OSINT Pentest Checklist

## 1. General Information

- [ ] Identify main domain  
  → Starting point of reconnaissance.
- [ ] Check Whois/RDAP (registrar, contacts)  
  → Collect ownership info, registrar, registration dates.
- [ ] Reverse WHOIS analysis  
  → Identify other domains registered with the same names, emails, or phone numbers found in WHOIS.
- [ ] Look up DNS history (SecurityTrails, DNSDB)  
  → Find past infrastructure and decommissioned assets.
- [ ] Search for public TLS certificates (crt.sh, censys.io)  
  → Discover subdomains and certificate issuance patterns.

## 2. DNS & Infrastructure Mapping
- [ ] Enumerate subdomains (Amass, Subfinder, crt.sh, VirusTotal…)  
  → Expands the attack surface by discovering new hosts.
- [ ] Validate DNS resolutions (A, AAAA, CNAME, MX, TXT)  
  → Confirm live infrastructure and linked services.
- [ ] Identify hosting providers / ASN / geolocation  
  → Detect cloud usage, ISPs, and potential regional exposure.

## 3. Services & Technologies
- [ ] Identify web servers (HTTP headers, Wappalyzer, whatweb)  
  → Detect frameworks, versions, and possible vulnerabilities.
- [ ] Detect CDN / WAF / load balancers  
  → Impacts attack surface and testing feasibility.
- [ ] Check mail servers (MX, SPF, DKIM, DMARC)  
  → Evaluate mail security and phishing risks.
- [ ] List exposed services (VPN, OWA, Citrix, SSH, RDP…)  
  → Entry points into the internal network.
- [ ] Verify vulnerable versions (banners, Shodan/Censys)  
  → Spot outdated or exploitable software.

## 4. Organizational Information
- [ ] Map employees on LinkedIn (linkedin2username)  
  → Build potential username lists.
- [ ] Identify technology stack via job postings / social media  
  → Reveal internal technologies in use.
- [ ] Search employees social media (Twitter, GitHub, Instagram)  
  → Can reveal technical info, internal tools, or sensitive content from posts/photos.
- [ ] Collect email addresses (hunter.io, theHarvester)  
  → Useful for phishing, password spraying, enumeration.
- [ ] Check for credential leaks (HIBP, dehashed, pastebin)  
  → Detect reused or compromised passwords.
- [ ] Identify partners / suppliers  
  → Supply chain attack vectors and related domains.
- [ ] Search for company phone numbers  
  → From website, social media, or public databases. Useful for social engineering.
- [ ] Find info on executives & public records (Pappers, Societe.ninja)  
  → Leadership details, company filings, financials, governance.

## 5. Public Files & Data
- [ ] Google Dorks (site:target.com, intitle, inurl, filetype…)  
  → Find exposed documents, directories, sensitive info indexed by search engines.
- [ ] Extract metadata (FOCA, ExifTool)  
  → Metadata leaks usernames, paths, software versions.
- [ ] Search related GitHub repositories (org/employees)  
  → May reveal credentials, API keys, or config files.
- [ ] Check exposed S3 / Azure Blob / GCP Storage buckets  
  → Cloud storage often contains sensitive information.
- [ ] Wayback Machine / archive.today  
  → Retrieve deleted pages or old versions of the website.
- [ ] Analyze photos of buildings/offices (Google Street View, employee social media)  
  → Can reveal badges, access controls, physical security details.

## 6. Network Surface
- [ ] Map services with Shodan, Censys, ZoomEye  
  → Identify what is exposed to the internet.
- [ ] Check if old IPs are still active (passive DNS)  
  → Legacy systems may be forgotten and unpatched.
- [ ] Analyze SSL/TLS certificates (strength, expiration, self-signed)  
  → Weak crypto or expired certs reduce trust/security.
