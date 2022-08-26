# Kerberoast

## Attack

### Find users "kerberoastable"

`dsquery * "dc=contoso,dc=com" -filter "(&(objectcategory=user)(servicePrincipalName=*))" -attr distinguishedName servicePrincipalName`

or in Powershell

```powershell
$S = New-Object DirectoryServices.DirectorySearcher
$S.Filter = '(&(objectcategory=user)(servicePrincipalName=*))'
$S.SearchRoot = 'LDAP://DC=contoso,DC=com'
$S.FindAll()
```

## Defenses

- clear the Service Principal Name (SPN) attribute of the user after checking that the host and service no longer exist.
If this in the case, transition the service to use a computer account. and ensure the process handling auth runs as system.

- give the user an unbreakable password - Andy Robbins recommends a password of 64 chars.
Then reconfigure the service by doing the auth kerberos to start as a user with the correct password.
