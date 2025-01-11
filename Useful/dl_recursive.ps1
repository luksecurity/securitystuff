param (
    [string]$url = "<URL>" 
)

function Download-FilesRecursively {
    param (
        [string]$url,
        [string]$downloadPath = "."
    )
    
    if (!(Test-Path -Path $downloadPath)) {
        New-Item -ItemType Directory -Path $downloadPath | Out-Null
    }

    try {
        $response = Invoke-WebRequest -Uri $url -UseBasicParsing
    } catch {
        Write-Error "Erreur lors de la connexion à $url"
        return
    }
    
    $links = $response.Links | ForEach-Object { $_.href }

    foreach ($link in $links) {
      
        if ($link -notmatch "^http") {
            $link = $url.TrimEnd('/') + '/' + $link.TrimStart('/')
        }

        if ($link -match "\.[a-zA-Z0-9]+$") {
            $fileName = Split-Path -Leaf $link
            $filePath = Join-Path -Path $downloadPath -ChildPath $fileName
            Write-Output "Téléchargement de $link vers $filePath"
            try {
                Invoke-WebRequest -Uri $link -OutFile $filePath
            } catch {
                Write-Error "Échec du téléchargement de $link"
            }
        } else {
            
            $subFolder = Split-Path -Leaf $link
            $subFolderPath = Join-Path -Path $downloadPath -ChildPath $subFolder
            Download-FilesRecursively -url $link -downloadPath $subFolderPath
        }
    }
}

Download-FilesRecursively -url $url -downloadPath (Get-Location)
