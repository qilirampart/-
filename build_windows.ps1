param(
    [switch]$Clean
)

$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

if ($Clean) {
    if (Test-Path build) {
        Remove-Item build -Recurse -Force
    }
    if (Test-Path dist) {
        Remove-Item dist -Recurse -Force
    }
}

$python = "python"
$pyinstallerVersion = & $python -m PyInstaller --version
Write-Host "PyInstaller $pyinstallerVersion"

& $python -m PyInstaller --noconfirm zhenxi.spec

$distRoot = Join-Path $projectRoot "dist\\zhenxi"
if (-not (Test-Path $distRoot)) {
    throw "Build failed: dist\\zhenxi was not generated."
}

Write-Host ""
Write-Host "Build finished: $distRoot"
Write-Host "Zip the whole dist\\zhenxi folder before sending it to other users."
