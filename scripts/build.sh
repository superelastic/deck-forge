#!/bin/bash

# Deck Forge Build Script
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
THEMES_DIR="$PROJECT_ROOT/themes"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_marp() {
    if ! command -v marp &> /dev/null; then
        echo -e "${RED}Error: Marp CLI not found. Install with: npm install -g @marp-team/marp-cli${NC}"
        exit 1
    fi
}

run_marp() {
    local input="$1"
    local format="$2"
    local output_dir="$3"
    
    local filename=$(basename "$input" .md)
    local output_file=""
    local format_arg=""
    
    case "$format" in
        html) output_file="$output_dir/${filename}.html"; format_arg="--html" ;;
        pdf)  output_file="$output_dir/${filename}.pdf";  format_arg="--pdf" ;;
        pptx) output_file="$output_dir/${filename}.pptx"; format_arg="--pptx" ;;
    esac
    
    mkdir -p "$output_dir"
    echo -e "${YELLOW}Building $format...${NC}"
    
    local theme_files=()
    while IFS= read -r -d '' theme_file; do
        theme_files+=("$theme_file")
    done < <(find "$THEMES_DIR" -name "*.css" -print0 2>/dev/null)

    if [[ ${#theme_files[@]} -gt 0 ]]; then
        marp "$input" -o "$output_file" $format_arg --theme-set "${theme_files[@]}"
    else
        marp "$input" -o "$output_file" $format_arg
    fi
    echo -e "${GREEN}Created: $output_file${NC}"
}

preview() {
    local input="$1"
    echo -e "${YELLOW}Starting preview server... Press Ctrl+C to stop${NC}"

    local theme_files=()
    while IFS= read -r -d '' theme_file; do
        theme_files+=("$theme_file")
    done < <(find "$THEMES_DIR" -name "*.css" -print0 2>/dev/null)

    if [[ ${#theme_files[@]} -gt 0 ]]; then
        marp "$input" --preview --html --theme-set "${theme_files[@]}"
    else
        marp "$input" --preview --html
    fi
}

# Main
COMMAND="$1"
INPUT="$2"
OUTPUT_DIR="${3:-./output}"

[[ -z "$COMMAND" || -z "$INPUT" ]] && { echo "Usage: $0 <preview|html|pdf|pptx|all> <file.md> [output_dir]"; exit 1; }
[[ ! -f "$INPUT" ]] && { echo -e "${RED}Error: File not found: $INPUT${NC}"; exit 1; }

check_marp

case "$COMMAND" in
    preview) preview "$INPUT" ;;
    html)    run_marp "$INPUT" "html" "$OUTPUT_DIR" ;;
    pdf)     run_marp "$INPUT" "pdf" "$OUTPUT_DIR" ;;
    pptx)    run_marp "$INPUT" "pptx" "$OUTPUT_DIR" ;;
    all)     run_marp "$INPUT" "html" "$OUTPUT_DIR"
             run_marp "$INPUT" "pdf" "$OUTPUT_DIR"
             run_marp "$INPUT" "pptx" "$OUTPUT_DIR" ;;
    *)       echo "Unknown command: $COMMAND"; exit 1 ;;
esac
