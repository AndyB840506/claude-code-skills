# Skill Test Harness - PS 5.1 compatible
# Static quality analysis for all Claude Code skill files

$globalPath  = "C:\Users\andre\.claude\skills"
$projectPath = "E:\Claude Project\Claude Projects\kit-skill-creator\.claude\skills"
$reportPath  = "E:\Claude Project\Claude Projects\kit-skill-creator\test-harness\results.md"

function Invoke-SkillCheck {
    param(
        [string]$SkillName,
        [string]$SkillFile,
        [string]$Source
    )

    $content   = Get-Content $SkillFile -Raw
    $lineCount = (Get-Content $SkillFile).Count

    $checks = [ordered]@{
        has_triggers      = ($content -match "(?i)(trigger|Triggers:|invoca|llama|type /|write /|escribe /|disparador)")
        has_welcome       = ($content -match "(?i)(bienvenid|welcome|hola |buenos|empez|inicio|start here|begin)")
        has_question_flow = ($content -match "(\b[1-9]\.|Paso |Step |pregunta|question|pide |asks? )")
        has_output_spec   = ($content -match "(?i)(genera|crea |output|produce|devuelve|returns|HTML|Markdown|JSON|reporte|entrega|archivo|report)")
        not_shallow       = ($lineCount -ge 25)
        no_placeholders   = (-not ($content -cmatch "\bTODO\b|\bTBD\b|\[INSERT\]|\[placeholder\]|\[YOUR_"))
        has_completion    = ($content -match "(?i)(termina|done|completo|finaliza|complete|resumen|summary|entrega|listo|handoff|cierre)")
    }

    $failed = @()
    $passed = 0
    foreach ($key in $checks.Keys) {
        if ($checks[$key]) {
            $passed++
        } else {
            $failed += $key
        }
    }

    return [PSCustomObject]@{
        Skill   = $SkillName
        Source  = $Source
        File    = $SkillFile
        Lines   = $lineCount
        Passed  = $passed
        Total   = $checks.Count
        Failed  = ($failed -join ", ")
        Score   = [math]::Round(($passed / $checks.Count) * 100)
    }
}

# Collect all SKILL.md files from both locations
$rawFiles = @()
if (Test-Path $globalPath) {
    $rawFiles += Get-ChildItem $globalPath  -Recurse -Filter "SKILL.md"
}
if (Test-Path $projectPath) {
    $rawFiles += Get-ChildItem $projectPath -Recurse -Filter "SKILL.md"
}

# Build display name from parent folder path
$allResults = @()
foreach ($file in $rawFiles) {
    $relName = $file.DirectoryName
    $relName = $relName -replace [regex]::Escape($globalPath),  "global:"
    $relName = $relName -replace [regex]::Escape($projectPath), "project:"
    $relName = $relName -replace "\\", "/"

    $source = "global"
    if ($file.FullName -like "*kit-skill-creator*") {
        $source = "project"
    }

    $result = Invoke-SkillCheck -SkillName $relName -SkillFile $file.FullName -Source $source
    $allResults += $result

    $status = "PASS"
    if ($result.Score -lt 70) { $status = "FAIL" }
    elseif ($result.Score -lt 100) { $status = "WARN" }

    Write-Host ("[$status] " + $result.Skill + " | " + $result.Score + "% | " + $result.Lines + " lines")
    if ($result.Failed) {
        Write-Host ("       Missing: " + $result.Failed)
    }
}

# Summary
$passing = ($allResults | Where-Object { $_.Score -ge 85 }).Count
$warning = ($allResults | Where-Object { $_.Score -ge 70 -and $_.Score -lt 85 }).Count
$failing = ($allResults | Where-Object { $_.Score -lt 70 }).Count
$total   = $allResults.Count

Write-Host ""
Write-Host ("=== RESULTS: " + $passing + " pass / " + $warning + " warn / " + $failing + " fail  (total " + $total + ") ===")

# Write markdown report
$lines = @()
$lines += "# Skill Test Harness Results"
$lines += ""
$lines += ("Run: " + (Get-Date -Format "yyyy-MM-dd HH:mm"))
$lines += ""
$lines += ("| Skill | Score | Lines | Missing checks |")
$lines += ("|-------|-------|-------|---------------|")

foreach ($r in ($allResults | Sort-Object Score)) {
    $status = "PASS"
    if ($r.Score -lt 70) { $status = "FAIL" }
    elseif ($r.Score -lt 100) { $status = "WARN" }
    $lines += ("| " + $r.Skill + " | " + $status + " " + $r.Score + "% | " + $r.Lines + " | " + $r.Failed + " |")
}

$lines += ""
$lines += ("**Total:** " + $passing + " pass / " + $warning + " warn / " + $failing + " fail out of " + $total)

$lines | Out-File $reportPath -Encoding utf8
Write-Host ("Report written to: " + $reportPath)
