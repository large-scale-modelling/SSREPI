#!/usr/bin/env bash
export PYTHONPATH = "..\lib;$PYTHONPATH"
cat .\miracle-specification-start.md > miracle-specification.md 
if command -v record-documentation.py >/dev/null 2>&1; then
	record-documentation.py >> miracle-specification-body.md
	cat miracle-specification-body.md >> miracle-specification.md
elif [ -f .\miracle-specification-body.md ]
then
	cat miracle-specification-body.md >> miracle-specification.md
else
	echo "Error: Python or record-documentation.py not found, and miracle-specification-body.md does not exist."
	exit 255
fi
cat .\miracle-specification-end.md > .\miracle-specification.md

# The order of these parameter is immportant

pandoc miracle-specification.md \
	--standalone 
        --toc \
	--number-sections \
        -o miracle-specification-full.tex \
        --filter=.\pandoc-crossref \
        --citeproc \
        --pdf-engine=xelatex \
	-V mainfont="Carlito-Regular.ttf" \
	-V mainfontoptions="BoldFont=Carlito-Bold.ttf,ItalicFont=Carlito-Italic.ttf,BoldItalicFont=Carlito-BoldItalic.ttf" \
        -V geometry:margin=1in \
        --bibliography=citations.bib

