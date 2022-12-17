# asp, aspx file upload bypass

## When he accepts images files (.jpg / .png / .gif)

### Fuzzing of accepted extensions

- create extensions list
- intercept request burp -> intruder
- click on clear and add the extension of the filename input
- click on Payloads tab and add the list of extensions
- click on start attack

If the config extension is accepted, you can use the file web.config to have an RCE.
https://lonewolfzero.wordpress.com/2018/05/28/rce-by-uploading-a-web-config-asp/

## Sources

- Repo PayloadsAllTheThings - swissky | web.config
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Configuration%20IIS%20web.config/web.config

- RCE by upload a web.config asp
https://lonewolfzero.wordpress.com/2018/05/28/rce-by-uploading-a-web-config-asp/
