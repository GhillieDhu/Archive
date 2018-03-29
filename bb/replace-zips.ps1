Import-Module Pscx

function test-zip {
    $zip = $args[0]
    $contents = Read-Archive $zip
    $expandable = $contents.Count -gt 0
    foreach($item in $contents) {
        $expandable = $expandable -and !$item.IsEncrypted
    }
    if($expandable){
        $unzip = $zip.FullName.Replace(".zip", "_zip")
        if(!(Test-Path $unzip)) {
            New-Item -Path $unzip -ItemType directory
        }
        Expand-Archive $zip $unzip
        return $True
    }
    else {
        return $False
    }
}

$zipList = $args[0]
$zipCount = 0
$zipsLength = 0
foreach($zip in $zipList) {
    $zipsLength += $zip.Length
}
$zipListCount = $zipList.Count
$unzipLength = 0
foreach($zip in $zipList) {
    $unzipLength += $zip.Length
    $zipCount += 1
    if (test-zip $zip) {
        Write-Host -NoNewline "$zipCount / $zipListCount : "
        $lengthFrac = ("{0:D3}" -f $unzipLength) / ("{0:D3}" -f $zipsLength)
        Write-Host -NoNewline ("{0:N2}" -f $lengthFrac)
        Write-Host " "$zip.FullName
        if(Test-Path $args[1]) {
            $null = Read-Host "Paused"
            Write-Host "Resumed"
        }
        if(Test-Path $args[2]) {
            break
        }
        Remove-Item $zip.FullName
    }
}