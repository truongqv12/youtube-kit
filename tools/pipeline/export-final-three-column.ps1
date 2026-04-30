param(
    [Parameter(Mandatory=$true)][string]$Channel,
    [Parameter(Mandatory=$true)][string]$Video,
    [string]$PythonPath = "python"
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..")
$PythonScript = Join-Path $RepoRoot "tools\pipeline\export-final-three-column.py"
$ArgsList = @($PythonScript, "--channel", $Channel, "--video", $Video)

Write-Host "Running final three-column export for channel=$Channel video=$Video"
& $PythonPath @ArgsList
exit $LASTEXITCODE
