# Cheatsheet

## Active Directory

### Kerberoast

Find users "kerberoastable"

`dsquery * "dc=contoso,dc=com" -filter "(&(objectcategory=user)(servicePrincipalName=*))" -attr distinguishedName servicePrincipalName`

or in Powershell

```powershell
$S = New-Object DirectoryServices.DirectorySearcher
$S.Filter = '(&(objectcategory=user)(servicePrincipalName=*))'
$S.SearchRoot = 'LDAP://DC=contoso,DC=com'
$S.FindAll()
```
