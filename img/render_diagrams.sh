#!/usr/bin/env bash
# Renders diagrams/diagram-NN.mmd -> img/diagram-NN.png
# Run this from the same directory as this script (the one containing
# diagrams/ and img/), on a machine where mmdc/Chromium actually works.

set -euo pipefail

mkdir -p img

if ! command -v mmdc &>/dev/null; then
    echo "mmdc not found. Install with:"
    echo "  npm install -g @mermaid-js/mermaid-cli"
    exit 1
fi

for f in diagrams/diagram-*.mmd; do
    name=$(basename "$f" .mmd)
    echo "Rendering $name..."
    mmdc -i "$f" -o "img/${name}.png" -w 1000 -b white
done

echo "Done. PNGs are in img/"
