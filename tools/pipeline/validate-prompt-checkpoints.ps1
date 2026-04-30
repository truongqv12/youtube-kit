param(
    [Parameter(Mandatory=$true)][string]$Channel,
    [Parameter(Mandatory=$true)][string]$Video,
    [string]$PythonPath = "python",
    [switch]$Report
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..")
$PythonScript = Join-Path $RepoRoot "tools\pipeline\validate-prompt-checkpoints.py"
$ArgsList = @($PythonScript, "--channel", $Channel, "--video", $Video)
if ($Report) { $ArgsList += "--report" }

Write-Host "Running checkpoint validation for channel=$Channel video=$Video"
& $PythonPath @ArgsList
exit $LASTEXITCODE
