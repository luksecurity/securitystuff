New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT | Out-Null

$outputFileWithService = ".\CLSID_WithService.txt"
$outputFileWithoutService = ".\CLSID_WithoutService.txt"

$withService = @()
$withoutService = @()

$CLSID = Get-ItemProperty HKCR:\clsid\* | Select-Object AppID,@{N="CLSID"; E={$_.PSChildName}} | Where-Object {$_.AppID -ne $null}

foreach ($a in $CLSID) {
    $clsid = $a.CLSID
    $appid = $a.AppID
    $entry = "CLSID: $clsid - AppID: $appid"

    $appPath = "HKCR:\AppID\$appid"
    if (Test-Path $appPath) {
        $appProperties = Get-ItemProperty -Path $appPath
        
        if ($appProperties.LocalService) {
            $entry += "`n -> Service Name: $($appProperties.LocalService)`n"
            $withService += $entry
        } else {
            $entry += "`n -> No service name associated.`n"
            $withoutService += $entry
        }
    } else {
        $entry += "`n -> AppID not found in AppID registry key.`n"
        $withoutService += $entry
    }
}

$withService | Out-File -FilePath $outputFileWithService
$withoutService | Out-File -FilePath $outputFileWithoutService

Write-Host "Export completed!"
Write-Host " -> CLSID with service: $outputFileWithService"
Write-Host " -> CLSID without service: $outputFileWithoutService"
