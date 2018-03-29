Import-Module Pscx

# % {$_.fullname.replace(from, (Get-Location).path)}

function extract-zip {
    $zip = $args[0]
    $tmpdir = $args[1]
    Expand-Archive $zip $tmpdir
    $tmpitems = Get-ChildItem -force -recurse $tmpdir
    $tmp256 = @{}
    foreach($item in $tmpitems) {
        if(!$item.PSIsContainer) {
            $item256 = Get-Hash $item -algorithm "sha256"
            if($tmp256.ContainsKey($item256.HashString)) {
                $tmp256.Set_Item($item256.HashString, $tmp256.Get_Item() + @($item256.Path))
            }
            else {
                $tmp256.Set_Item($item256.HashString, @($item256.Path))
            }
        }
    }
    return $tmp256
}

function test-zip {
    $zip = $args[0]
    $contents = Read-Archive $zip
    $expandable = $True
    foreach($item in $contents) {
        $expandable = $expandable -and !$item.IsEncrypted
    }
    if($expandable){
        Expand-Archive $zip $args[1]
        return $True
    }
    else {
        return $False
    }
}

$basedir = $args[1]
$tmpdir = New-Item -type directory -path "$basedir\temp"
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
    "$zipCount / $zipListCount"
    $unzipLength / $zipsLength
    if (test-zip $zip $tmpdir) {
        $file256 = Import-Clixml $args[2]
        $linkBasePath = $zip.FullName.Replace(".", "_")
        if(!(Test-Path($linkBasePath))) {
            New-Item -Path $linkBasePath -ItemType directory
        }
        $tmpitems = Get-ChildItem -force -recurse $tmpdir
        foreach($item in $tmpitems) {
            if(!$item.PSIsContainer) {
                $newPath = ($item.Directory.FullName).Replace($tmpdir, $linkBasePath)
                if(!(Test-Path($newPath))) {
                    New-Item -Path $newPath -ItemType directory
                }
                $item256 = Get-Hash $item -Algorithm SHA256
                $itemHash = $item256.HashString
                if($file256.ContainsKey($itemHash)) {
                    $targetList = $file256.Get_Item($itemHash)
                    $linkTarget = $targetList[0]
                    $linkPath = $item.FullName.Replace($tmpdir, $linkBasePath)+".lnk"
                    $link = (New-Object -ComObject WScript.Shell).CreateShortcut($linkPath)
                    $link.TargetPath = $linkTarget
                    $link.Save()
                }
                else {
                    $movedItem = $item.FullName.Replace($tmpdir, $linkBasePath)
                    Move-Item $item.FullName $movedItem
                    $file256.Set_Item($item256.HashString, @($movedItem))
                }
            }
        }
        Export-Clixml -InputObject $file256 -Path $args[2]
        if(Test-Path($args[3])) {
            $null = Read-Host "Paused"
            Write-Host "Resumed"
        }
        if(Test-Path($args[4])) {
            break
        }
        Remove-Item $zip
    }
    Remove-Item -force -recurse "$tmpdir\*"
}
Remove-Item $tmpdir