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
pandoc .\miracle-specification.md --standalone --toc --citeproc --bibliography=citations.bib -o miracle-specification-full.tex

