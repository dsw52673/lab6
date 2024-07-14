$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Error "Python is not installed. Please install Python first."
    exit 1
}

$pip = Get-Command pip -ErrorAction SilentlyContinue
if (-not $pip) {
    Write-Error "pip is not installed. Please install pip first."
    exit 1
}

$pip install xmltodict
$pip install pyyaml

Write-Output "Dependencies installed successfully."
