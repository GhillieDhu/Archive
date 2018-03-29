import-module pscx

function get-recursivehash {
    $parent = get-item ($args[0])
    $children = Get-ChildItem $parent
    if ($children -ne $null) {
        foreach ($child in $children) {
            if ($child.PSIsContainer) {
                get-recursivehash $child.fullname
            }
            else {
                get-hash $child.fullname -algorithm "sha256"
            }
        }
    }
}

$allzips = Get-ChildItem -path $args[0] -force -recurse -include *.zip
$sortedzips = $allzips | sort-object -property length -descending
$shell = new-object -com shell.application
if ($sortedzips -ne $null) {
    foreach ($zip in $sortedzips) {
        write-host $zip.fullname
        $zipitems = ($shell.namespace($zip.fullname)).items()
        foreach ($item in $zipitems) {
            $shell.namespace((gl).path).copyhere($item)
            $copyitem = get-item ($args[1]+"\"+$item.name)
            if ($copyitem.PSIsContainer) {
                get-recursivehash $copyitem
            }
            else {
                get-hash $copyitem -algorithm "sha256"
            }
            remove-item -recurse $copyitem
        }
        write-host ""
    }
    #% {$shell.namespace((gl).path).copyhere( ($shell.namespace($_.fullname)).items() );}
}
#return $sortedzips
#$ozip | % {$subdir = $_.basename -replace ("\.", "_"); $_.directory.fullname+$subdir}
