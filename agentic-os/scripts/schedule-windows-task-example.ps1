<#
Optional OFFLINE structural check, not a scheduled Claude skill.
No task is registered unless -Register is passed explicitly.
Pass absolute paths to your Python executable, source clone, and workspace.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$PythonExe,
    [Parameter(Mandatory=$true)][string]$SourceRepository,
    [Parameter(Mandatory=$true)][string]$Workspace,
    [string]$TaskName = 'ClaudeAgenticOS-OfflineCheck',
    [switch]$Register
)
$ErrorActionPreference = 'Stop'
foreach ($taskPath in @($PythonExe, $SourceRepository, $Workspace)) {
    if (-not [IO.Path]::IsPathRooted($taskPath) -or $taskPath.Contains('"')) {
        throw 'Use absolute paths without quote characters.'
    }
    if (-not (Test-Path -LiteralPath $taskPath)) { throw "Path not found: $taskPath" }
}
$validatorPath = Join-Path $SourceRepository 'scripts/validate.py'
if (-not (Test-Path -LiteralPath $validatorPath -PathType Leaf)) { throw 'Source validator missing.' }
$taskArguments = '"' + $validatorPath + '" --root "' + $Workspace + '"'
if (-not $Register) {
    Write-Output 'Preview only. Would register a daily 09:00 offline check for the current user.'
    Write-Output "Task: $TaskName"
    Write-Output "Executable: $PythonExe"
    Write-Output "Arguments: $taskArguments"
    Write-Output 'Review first; pass -Register only when ready. No Claude calls or API charges.'
    return
}
if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    throw 'A task with this name already exists. Choose a different name or review the existing task.'
}
$taskAction = New-ScheduledTaskAction -Execute $PythonExe -Argument $taskArguments -WorkingDirectory $Workspace
$taskTrigger = New-ScheduledTaskTrigger -Daily -At '09:00'
$taskSettings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 5)
Register-ScheduledTask -TaskName $TaskName -Action $taskAction -Trigger $taskTrigger -Settings $taskSettings -Description 'Offline Agentic OS structural validation; no Claude execution.' | Out-Null
Get-ScheduledTask -TaskName $TaskName | Select-Object TaskName, State
