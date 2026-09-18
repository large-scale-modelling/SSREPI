$env:PYTHONPATH = "..\lib;$env:PYTHONPATH"
Get-Content .\miracle-specification-start.md | Set-Content .\miracle-specification.md 
if ((Get-Command python -ErrorAction SilentlyContinue) -and (Get-Command record-documentation.py -ErrorAction SilentlyContinue)) {
	python ..\bin\record-documentation.py | Add-Content .\miracle-specification.md
} elseif (Test-Path .\miracle-specification-body.md) {
	Get-Content .\miracle-specification-body.md | Add-Content .\miracle-specification.md
} else {
	Write-Host "Error: Python or record-documentation.py not found, and miracle-specification-body.md does not exist."
	exit
}
Get-Content .\miracle-specification-end.md | Add-Content .\miracle-specification.md

# The order of these parameter is immportant

pandoc miracle-specification.md `
  	--standalone `
        --toc `
        -o miracle-specification-full.tex `
        --filter=.\pandoc-crossref `
        --natbib `
        --pdf-engine=xelatex `
	-V mainfont="Carlito-Regular.ttf" `
	-V mainfontoptions="BoldFont=Carlito-Bold.ttf,ItalicFont=Carlito-Italic.ttf,BoldItalicFont=Carlito-BoldItalic.ttf" `
        -V geometry:margin=1in `
        --bibliography=citations.bib

