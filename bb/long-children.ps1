function Recurse-LongChild {
    New-PSDrive -Name Z -Root $args[0] -PSProvider FileSystem
    cd Z:\
    cd o
    Write-Host (Get-ChildItem)
    $children = Get-ChildItem .
    $descendents = $children
    foreach($child in $children) {
        #$child
        #$descendents += Recurse-LongChild $child
    }
    cd F:
    Remove-PSDrive Z
    return $children
    #return $descendents
}

$root = $args[0]

return Recurse-LongChild $root
#Recurse-LongChild $root