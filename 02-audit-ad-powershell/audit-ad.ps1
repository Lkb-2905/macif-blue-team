param(
    [string]$InputPath = "users.sample.json",
    [string]$OutputPath = "inactive_users.csv",
    [int]$Days = 90
)

$raw = Get-Content -Path $InputPath -Raw
$users = $raw | ConvertFrom-Json
$limit = (Get-Date).AddDays(-$Days)

$inactive = $users | Where-Object {
    $_.LastLogonDate -and ([datetime]$_.LastLogonDate) -lt $limit
}

$inactive | Select-Object Name, SamAccountName, LastLogonDate |
    Export-Csv -NoTypeInformation -Path $OutputPath

Write-Output "Export OK: $OutputPath"
