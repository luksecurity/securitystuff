# Check les applications qui ont des secrets
Get-MgApplication -All -Property displayName,appId,passwordCredentials | Where-Object { $_.PasswordCredentials } | select DisplayName,AppId,PasswordCredentials
