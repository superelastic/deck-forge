#!/usr/bin/env python3
"""
Index session markdown files into a FAISS vector store for semantic search.

Usage:
    python scripts/index_sessions.py [--rebuild]

Options:
    --rebuild   Force rebuild of entire index, ignoring cached state
"""

import json
import os
import re
import sys
from pathlib import Path

# Lazy imports for optional dependencies
def get_dependencies():
    """Import heavy dependencies only when needed."""
    try:
        from sentence_transformers import SentenceTransformer
        import faiss
        import numpy as np
        return SentenceTransformer, faiss, np
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Install with: pip install sentence-transformers faiss-cpu")
        sys.exit(1)


# Configuration
MODEL_NAME = "all-MiniLM-L6-v2"  # Fast, ~80MB, good quality
SESSION_LOGS_DIR = ".session_logs"
INDEX_DIR = f"{SESSION_LOGS_DIR}/.vector_index"
INDEX_FILE = f"{INDEX_DIR}/index.faiss"
METADATA_FILE = f"{INDEX_DIR}/metadata.json"
INDEXED_FILES_FILE = f"{INDEX_DIR}/indexed_files.txt"


def chunk_markdown(content: str, filepath: str) -> list[dict]:
    """
    Chunk markdown content by ## headers for granular retrieval.

    Returns list of dicts with:
        - text: chunk content
        - file: source file path
        - section: section header (or "intro" for content before first header)
    """
    chunks = []

    # Split by ## headers (keep the header with the content)
    sections = re.split(r'(?=^## )', content, flags=re.MULTILINE)

    for section in sections:
        section = section.strip()
        if not section:
            continue

        # Extract section title
        if section.startswith('## '):
            lines = section.split('\n', 1)
            title = lines[0].replace('## ', '').strip()
            text = lines[1].strip() if len(lines) > 1 else ""
        else:
            title = "intro"
            text = section

        # Skip very short chunks (< 50 chars) as they're not useful for search
        if len(text) < 50:
            continue

        # Truncate very long chunks to first 2000 chars for embedding efficiency
        if len(text) > 2000:
            text = text[:2000] + "..."

        chunks.append({
            "text": text,
            "file": filepath,
            "section": title,
            "preview": text[:200].replace('\n', ' ')
        })

    return chunks


def find_session_files(base_dir: str) -> list[Path]:
    """Find all markdown session files to index."""
    session_path = Path(base_dir)
    if not session_path.exists():
        return []

    # Find all .md files, excluding the vector index directory
    files = []
    for md_file in session_path.rglob("*.md"):
        # Skip files in .vector_index
        if ".vector_index" in str(md_file):
            continue
        files.append(md_file)

    return sorted(files)


def load_indexed_files() -> set[str]:
    """Load set of already-indexed file paths."""
    if not os.path.exists(INDEXED_FILES_FILE):
        return set()

    with open(INDEXED_FILES_FILE, 'r') as f:
        return set(line.strip() for line in f if line.strip())


def save_indexed_files(files: set[str]):
    """Save set of indexed file paths."""
    with open(INDEXED_FILES_FILE, 'w') as f:
        for filepath in sorted(files):
            f.write(f"{filepath}\n")


def load_existing_index():
    """Load existing FAISS index and metadata if they exist."""
    SentenceTransformer, faiss, np = get_dependencies()

    if not os.path.exists(INDEX_FILE) or not os.path.exists(METADATA_FILE):
        return None, []

    try:
        index = faiss.read_index(INDEX_FILE)
        with open(METADATA_FILE, 'r') as f:
            metadata = json.load(f)
        return index, metadata
    except Exception as e:
        print(f"Warning: Could not load existing index: {e}")
        return None, []


def build_index(rebuild: bool = False):
    """
    Build or update the FAISS index.

    Args:
        rebuild: If True, rebuild entire index from scratch
    """
    SentenceTransformer, faiss, np = get_dependencies()

    # Create index directory
    os.makedirs(INDEX_DIR, exist_ok=True)

    # Find all session files
    session_files = find_session_files(SESSION_LOGS_DIR)

    if not session_files:
        print("No session files found to index.")
        return

    # Load existing state
    if rebuild:
        indexed_files = set()
        existing_index = None
        existing_metadata = []
    else:
        indexed_files = load_indexed_files()
        existing_index, existing_metadata = load_existing_index()

    # Find new files to index
    new_files = [f for f in session_files if str(f) not in indexed_files]

    if not new_files and existing_index is not None:
        print(f"Index up to date ({len(indexed_files)} files indexed)")
        return

    print(f"Found {len(new_files)} new file(s) to index...")

    # Load model
    print(f"Loading embedding model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)
    embedding_dim = model.get_sentence_embedding_dimension()

    # Process new files
    new_chunks = []
    for filepath in new_files:
        try:
            content = filepath.read_text(encoding='utf-8')
            chunks = chunk_markdown(content, str(filepath))
            new_chunks.extend(chunks)
            indexed_files.add(str(filepath))
        except Exception as e:
            print(f"  Warning: Could not process {filepath}: {e}")

    if not new_chunks and existing_index is not None:
        print("No new content to index.")
        save_indexed_files(indexed_files)
        return

    # Generate embeddings for new chunks
    print(f"Generating embeddings for {len(new_chunks)} chunks...")
    texts = [chunk["text"] for chunk in new_chunks]
    new_embeddings = model.encode(texts, show_progress_bar=True)

    # Combine with existing index or create new
    if existing_index is not None and len(existing_metadata) > 0:
        # Add new embeddings to existing index
        existing_index.add(np.array(new_embeddings).astype('float32'))
        all_metadata = existing_metadata + new_chunks
        index = existing_index
    else:
        # Create new index
        index = faiss.IndexFlatIP(embedding_dim)  # Inner product for cosine similarity

        # Normalize embeddings for cosine similarity
        embeddings_array = np.array(new_embeddings).astype('float32')
        faiss.normalize_L2(embeddings_array)
        index.add(embeddings_array)
        all_metadata = new_chunks

    # Save index and metadata
    faiss.write_index(index, INDEX_FILE)
    with open(METADATA_FILE, 'w') as f:
        json.dump(all_metadata, f, indent=2)
    save_indexed_files(indexed_files)

    print(f"Index built: {index.ntotal} chunks from {len(indexed_files)} files")
    print(f"Index saved to: {INDEX_DIR}/")


def main():
    rebuild = "--rebuild" in sys.argv
    build_index(rebuild=rebuild)


if __name__ == "__main__":
    main()
