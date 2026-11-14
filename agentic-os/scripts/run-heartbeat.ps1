# Start one INTERACTIVE Claude session, with the heartbeat request prefilled.
$ErrorActionPreference = 'Stop'
$workspacePath = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$claudeCommand = Get-Command claude -ErrorAction SilentlyContinue
if (-not $claudeCommand) { throw 'Claude Code is not on PATH. See the official installation guide.' }
Push-Location -LiteralPath $workspacePath
try {
    & $claudeCommand.Source '/heartbeat'
    $claudeExitCode = $LASTEXITCODE
} finally {
    Pop-Location
}
exit $claudeExitCode
