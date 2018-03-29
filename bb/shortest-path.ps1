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
    
return shortest-path $args[0]