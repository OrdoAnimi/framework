$repoPath = "C:\Users\phill\Documents\GitHub\velocity-architecture"
$logPath  = Join-Path $repoPath "DEPLOYMENT-LOG.md"

$date    = Get-Date -Format 'yyyy-MM-dd'
$version = '4.0.0'

$changed = git -C $repoPath diff --name-only HEAD 2>$null
if (-not $changed) { $changed = git -C $repoPath diff --name-only --cached 2>$null }
$fileList = ($changed | Where-Object { $_ -ne '' }) -join ', '
if (-not $fileList) { $fileList = 'none' }

$entry = @"

## $date

**Version:** $version
**Files changed:** $fileList
**Summary:** Session end.
**Known issues:** None.

---
"@

Add-Content -Path $logPath -Value $entry
