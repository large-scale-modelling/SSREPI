# Renders diagrams\diagram-NN.mmd -> img\diagram-NN.png
# Run this from the same directory as this script (the one containing
# diagrams\ and img\), on a machine where mmdc/Chromium actually works.

$ErrorActionPreference = "Stop"

if (-not (Get-Command mmdc -ErrorAction SilentlyContinue)) {
    Write-Host "mmdc not found. Install with:"
    Write-Host "  npm install -g @mermaid-js/mermaid-cli"
    exit 1
}

Get-ChildItem -Path . -Filter "diagram-*.mmd" | ForEach-Object {
    $name = $_.BaseName
    Write-Host "Rendering $name..."
    mmdc -i $_.FullName -o "$name.png" -w 1000 -s 5 -b white
}

Write-Host "Done. PNGs are in ."
