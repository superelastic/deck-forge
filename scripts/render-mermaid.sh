#!/bin/bash

# Render Mermaid diagrams from markdown to SVG
# Usage: ./scripts/render-mermaid.sh <deck.md>
#
# Extracts ```mermaid blocks, renders to SVG in img/, and creates
# a new markdown file with image references replacing the code blocks.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_mmdc() {
    if ! command -v mmdc &> /dev/null; then
        echo -e "${RED}Error: Mermaid CLI not found. Install with: npm install -g @mermaid-js/mermaid-cli${NC}"
        exit 1
    fi
}

INPUT="$1"

if [[ -z "$INPUT" ]]; then
    echo "Usage: $0 <deck.md>"
    echo "Renders Mermaid diagrams to SVG and updates markdown with image references."
    exit 1
fi

if [[ ! -f "$INPUT" ]]; then
    echo -e "${RED}Error: File not found: $INPUT${NC}"
    exit 1
fi

check_mmdc

# Get directory of input file
INPUT_DIR="$(cd "$(dirname "$INPUT")" && pwd)"
INPUT_FILE="$(basename "$INPUT")"
IMG_DIR="$INPUT_DIR/img"

mkdir -p "$IMG_DIR"

echo -e "${YELLOW}Extracting and rendering Mermaid diagrams...${NC}"

# Create a temporary file for the output
OUTPUT="$INPUT_DIR/${INPUT_FILE%.md}.rendered.md"
cp "$INPUT" "$OUTPUT"

# Extract mermaid blocks, render them, and replace in output
DIAGRAM_NUM=0
TEMP_MMD=$(mktemp /tmp/mermaid.XXXXXX.mmd)

# Use awk to find and process mermaid blocks
awk '
    /^```mermaid/ {
        in_mermaid = 1
        block = ""
        next
    }
    /^```$/ && in_mermaid {
        in_mermaid = 0
        print "MERMAID_BLOCK_START"
        print block
        print "MERMAID_BLOCK_END"
        next
    }
    in_mermaid {
        block = block $0 "\n"
        next
    }
    { print }
' "$INPUT" > "$OUTPUT.tmp"

# Process the temp file to render each mermaid block
DIAGRAM_NUM=0
while IFS= read -r line; do
    if [[ "$line" == "MERMAID_BLOCK_START" ]]; then
        DIAGRAM_NUM=$((DIAGRAM_NUM + 1))
        MERMAID_CONTENT=""
        while IFS= read -r mline && [[ "$mline" != "MERMAID_BLOCK_END" ]]; do
            MERMAID_CONTENT+="$mline"$'\n'
        done

        # Write mermaid content to temp file
        echo "$MERMAID_CONTENT" > "$TEMP_MMD"

        # Render to SVG
        SVG_FILE="$IMG_DIR/diagram-$(printf '%02d' $DIAGRAM_NUM).svg"
        echo -e "  Rendering diagram $DIAGRAM_NUM..."

        if mmdc -i "$TEMP_MMD" -o "$SVG_FILE" -b transparent 2>/dev/null; then
            # Output image reference instead of mermaid block
            echo "![Diagram $DIAGRAM_NUM](img/$(basename "$SVG_FILE"))"
        else
            echo -e "${RED}  Failed to render diagram $DIAGRAM_NUM${NC}"
            echo '```mermaid'
            echo "$MERMAID_CONTENT"
            echo '```'
        fi
    else
        echo "$line"
    fi
done < "$OUTPUT.tmp" > "$OUTPUT"

rm -f "$OUTPUT.tmp" "$TEMP_MMD"

echo -e "${GREEN}Created: $OUTPUT${NC}"
echo -e "${GREEN}Rendered $DIAGRAM_NUM diagrams to $IMG_DIR/${NC}"
echo ""
echo "To preview: ./scripts/build.sh preview $OUTPUT"
