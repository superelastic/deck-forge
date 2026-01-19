#!/usr/bin/env python3
"""
Semantic search over session log vector index.

Usage:
    python scripts/semantic_filter.py "query string" [file1.md file2.md ...]

Arguments:
    query       The search query (full question works best)
    files       Optional: limit search to specific files

Output:
    Ranked results with similarity scores, one per line:
    0.876 - path/to/file.md (Section: header)
"""

import json
import os
import sys
from pathlib import Path


def get_dependencies():
    """Import heavy dependencies only when needed."""
    try:
        from sentence_transformers import SentenceTransformer
        import faiss
        import numpy as np
        return SentenceTransformer, faiss, np
    except ImportError as e:
        print(f"Missing dependency: {e}", file=sys.stderr)
        print("Install with: pip install sentence-transformers faiss-cpu", file=sys.stderr)
        sys.exit(1)


# Configuration
MODEL_NAME = "all-MiniLM-L6-v2"
SESSION_LOGS_DIR = ".session_logs"
INDEX_DIR = f"{SESSION_LOGS_DIR}/.vector_index"
INDEX_FILE = f"{INDEX_DIR}/index.faiss"
METADATA_FILE = f"{INDEX_DIR}/metadata.json"

# Search parameters
TOP_K = 5  # Number of results to return by default


def load_index():
    """Load FAISS index and metadata."""
    SentenceTransformer, faiss, np = get_dependencies()

    if not os.path.exists(INDEX_FILE) or not os.path.exists(METADATA_FILE):
        print("No index found. Run: python scripts/index_sessions.py", file=sys.stderr)
        sys.exit(1)

    try:
        index = faiss.read_index(INDEX_FILE)
        with open(METADATA_FILE, 'r') as f:
            metadata = json.load(f)
        return index, metadata
    except Exception as e:
        print(f"Error loading index: {e}", file=sys.stderr)
        sys.exit(1)


def search(query: str, file_filter: list[str] | None = None, top_k: int = TOP_K) -> list[dict]:
    """
    Search the index for chunks matching the query.

    Args:
        query: Search query string
        file_filter: Optional list of file paths to limit search to
        top_k: Number of results to return

    Returns:
        List of dicts with: score, file, section, preview
    """
    SentenceTransformer, faiss, np = get_dependencies()

    index, metadata = load_index()

    # Load model and encode query
    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode([query])

    # Normalize for cosine similarity
    query_array = np.array(query_embedding).astype('float32')
    faiss.normalize_L2(query_array)

    # Search - get more results if filtering by file
    search_k = top_k * 10 if file_filter else top_k
    scores, indices = index.search(query_array, min(search_k, index.ntotal))

    # Collect results
    results = []
    seen_files = set()

    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(metadata):
            continue

        chunk = metadata[idx]
        filepath = chunk["file"]

        # Apply file filter if specified
        if file_filter:
            # Normalize paths for comparison
            filepath_normalized = str(Path(filepath))
            if not any(filepath_normalized.endswith(f) or f in filepath_normalized
                      for f in file_filter):
                continue

        # Deduplicate by file (return best chunk per file)
        if filepath in seen_files:
            continue
        seen_files.add(filepath)

        results.append({
            "score": float(score),
            "file": filepath,
            "section": chunk.get("section", ""),
            "preview": chunk.get("preview", "")
        })

        if len(results) >= top_k:
            break

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/semantic_filter.py \"query\" [file1 file2 ...]")
        print()
        print("Examples:")
        print('  python scripts/semantic_filter.py "OAuth authentication"')
        print('  python scripts/semantic_filter.py "rate limiting" file1.md file2.md')
        sys.exit(1)

    query = sys.argv[1]
    file_filter = sys.argv[2:] if len(sys.argv) > 2 else None

    results = search(query, file_filter)

    if not results:
        print("No matching results found.", file=sys.stderr)
        sys.exit(0)

    # Output in format expected by RETRIEVAL_PROTOCOL
    for result in results:
        section_info = f" (Section: {result['section']})" if result['section'] else ""
        print(f"  {result['score']:.3f} - {result['file']}{section_info}")


if __name__ == "__main__":
    main()
