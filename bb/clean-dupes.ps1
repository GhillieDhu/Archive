function shortest-path {
    $hashish = $args[0]
    $hashout = @{}
    foreach($hashKey in $hashish.Keys) {
        if($hashish.Get_Item($hashKey).Count -gt 1) {
            $dupes = @{}
            $minLength = 500
            foreach($path in $hashish.Get_Item($hashKey)) {
                $dupes.Set_Item($path.Length, $path)
            }
            $minLength = [Math]::min($path.Length, $minLength)
            $hashout.Set_Item($hashKey, $dupes.Get_Item($minLength))
        }
    }
    return $hashout
}


function replace-with-shortcut {
    $shortest_paths = $args[0]
    $all_paths = $args[1]
    foreach($key in $shortest_paths.Keys) {
        $short_path = $shortest_paths.Get_Item($key)
        foreach($path in $all_paths.Get_Item($key)) {
            if($path -ne $short_path) {
                $shortcut = $path+".lnk"
                $link = (New-Object -ComObject WScript.Shell).CreateShortcut($shortcut)
                $link.TargetPath = $short_path
                try {
                    $link.Save()
                    Remove-Item $path
                    Write-Host -NoNewline "."
                }
                catch {
                    Write-Host $path
                }
            }
        }
    }
}
    
$all_paths = $args[0]
$shortest_paths = shortest-path $all_paths

replace-with-shortcut $shortest_paths $all_paths