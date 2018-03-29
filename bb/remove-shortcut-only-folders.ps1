function remove-shortcut-only-folders {
    $count = 1
    while ($count -gt 0) {
        $dirs = Get-ChildItem -Directory -Recurse
        $linkonly = $dirs | % {if((Get-ChildItem -Exclude *.lnk $_.FullName).Count -eq 0) {$_}}
        $count = $linkonly.Count
        Write-Host($count)
        $linkonly | % {Remove-Item -Recurse $_.FullName}
    }
}
    
remove-shortcut-only-folders