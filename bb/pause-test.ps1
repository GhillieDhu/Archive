while($true) {
    Get-Date
    Start-Sleep -Seconds 10
    if(Test-Path $args[0]) {
        $null = Read-Host "Paused"
    }
    if(Test-Path $args[1]) {
        break
    }
}