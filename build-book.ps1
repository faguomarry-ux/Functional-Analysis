param(
    [ValidateSet('book', 'example')]
    [string]$Target = 'book'
)
$ErrorActionPreference = 'Stop'
Push-Location -LiteralPath $PSScriptRoot
try {
    $engine = Get-Command xelatex -ErrorAction Stop
    $bookOutputDir = Join-Path $PSScriptRoot 'output/pdf'
    New-Item -ItemType Directory -Path $bookOutputDir -Force | Out-Null
    # \include writes per-chapter .aux files under the output directory.
    New-Item -ItemType Directory -Path (Join-Path $bookOutputDir 'books') -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $bookOutputDir 'books/yosida') -Force | Out-Null
    $source = if ($Target -eq 'book') { 'main.tex' } else { 'example.tex' }
    for ($pass = 1; $pass -le 3; $pass++) {
        Write-Host "[BUILD] $source, pass $pass/3"
        & $engine.Source '-interaction=nonstopmode' '-halt-on-error' '-file-line-error' '-synctex=1' "-output-directory=$bookOutputDir" $source
        if ($LASTEXITCODE -ne 0) {
            throw "XeLaTeX failed on pass $pass. Check the log in $bookOutputDir."
        }
    }
    $pdfName = [System.IO.Path]::ChangeExtension($source, '.pdf')
    Write-Host "[OK] $(Join-Path $bookOutputDir $pdfName)"
}
finally {
    Pop-Location
}
