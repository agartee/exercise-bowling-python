$rootDir = (get-item $PSScriptRoot).Parent.FullName

# **************************************************************************************
# Deactivate Python Virtual Environment
# **************************************************************************************
deactivate | Out-Null

# **************************************************************************************
# Delete Python Virtual Environment (if exists)
# **************************************************************************************
$venvPath = "$($rootDir)\.venv"

if (Test-Path -Path $venvPath) {
    Remove-Item -Recurse -Force "$($venvPath)"
    Write-Host "Python virtual environment deleted." -ForegroundColor Green
}

# **************************************************************************************
# Delete pytest Cache (if exists)
# **************************************************************************************
$pytestCachePath = "$($rootDir)\.pytest_cache"

if (Test-Path -Path $pytestCachePath) {
    Remove-Item -Recurse -Force "$($pytestCachePath)"
    Write-Host "pytest cache deleted." -ForegroundColor Green
}

# **************************************************************************************
# Delete pytest Coverage File (if exists)
# **************************************************************************************
$pytestCoverageFilePath = "$($rootDir)\.coverage"

if (Test-Path -Path $pytestCoverageFilePath) {
    Remove-Item "$($pytestCoverageFilePath)"
    Write-Host "pytest coverage file deleted." -ForegroundColor Green
}

# **************************************************************************************
# Bootstrap
# **************************************************************************************
& "$($rootDir)\scripts\bootstrap.ps1"
