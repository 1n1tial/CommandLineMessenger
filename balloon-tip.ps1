function ShowBalloonTipInfo {    
    [CmdletBinding()]
    param (
        [string]$Title,
        [string]$Text,
        # It must be 'None', 'Info', 'Warning', 'Error'
        [string]$Icon = 'Info'
    )
    
    Add-Type -AssemblyName System.Windows.Forms
    
    if ($null -eq $script:balloonToolTip) {
        $script:balloonToolTip = New-Object System.Windows.Forms.NotifyIcon 
    }
    
    $path = Get-Process -id $pid | Select-Object -ExpandProperty Path
    $balloonToolTip.Icon = [System.Drawing.Icon]::ExtractAssociatedIcon($path)
    $balloonToolTip.BalloonTipIcon = $Icon
    $balloonToolTip.BalloonTipText = $Text
    $balloonToolTip.BalloonTipTitle = $Title
    $balloonToolTip.Visible = $true

    $balloonToolTip.ShowBalloonTip(3000)
}

