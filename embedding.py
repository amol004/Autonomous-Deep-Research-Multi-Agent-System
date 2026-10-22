# Document & PDF Vector Embedding Generator
# Uses Google EmbeddingGemma-2 (740M) via Ollama / OpenAI API.
#
# Supported file formats: .pdf, .txt, .md, .py, .json, .csv, .docx
# Requirements:
# uv pip install pypdf python-dotenv openai

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables (.env)
load_dotenv()

# Initialize OpenAI-compatible client (pointing to Ollama)
client = OpenAI(
    base_url=os.getenv("BASE_URL", "http://localhost:11434/v1"),
    api_key=os.getenv("API_KEY", "ollama")
)

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "embeddinggemma-2:740m")


def clean_file_path(raw_path: str) -> str:
    """Clean and expand a file path (removes quotes, resolves escaped spaces and ~)."""
    if not raw_path:
        return ""
    # Strip quotes often added when dragging and dropping into terminal
    cleaned = raw_path.strip().strip("'\"").strip()
    # Unescape escaped spaces from terminal drag-and-drop (e.g. 'My\ File.pdf')
    cleaned = cleaned.replace("\\ ", " ")
    return str(Path(os.path.expanduser(cleaned)).resolve())


def extract_text_from_pdf(file_path: str) -> tuple[str, int]:
    """
    Extract text content and page count from a PDF file using pypdf.
    """
    try:
        from pypdf import PdfReader
    except ImportError:
        raise ImportError(
            "The 'pypdf' library is required to read PDF files.\n"
            "Install it using: uv pip install pypdf"
        )

    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    extracted_pages = []

    for idx, page in enumerate(reader.pages):
        page_text = page.extract_text() or ""
        if page_text.strip():
            extracted_pages.append(f"--- Page {idx + 1} ---\n{page_text.strip()}")

    full_text = "\n\n".join(extracted_pages).strip()
    return full_text, total_pages


def extract_text_from_docx(file_path: str) -> str:
    """Extract text content from a Word (.docx) document."""
    try:
        import docx
    except ImportError:
        raise ImportError(
            "The 'python-docx' library is required to read .docx files.\n"
            "Install it using: uv pip install python-docx"
        )

    doc = docx.Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs).strip()


def load_document(file_path: str) -> tuple[str, dict]:
    """
    Load and extract text from a file based on its extension.
    Returns (extracted_text, metadata_dict).
    """
    resolved_path = clean_file_path(file_path)

    if not os.path.exists(resolved_path):
        raise FileNotFoundError(f"File not found: '{file_path}' (resolved: '{resolved_path}')")

    if not os.path.isfile(resolved_path):
        raise ValueError(f"Path is not a regular file: '{resolved_path}'")

    path_obj = Path(resolved_path)
    extension = path_obj.suffix.lower()
    file_size = os.path.getsize(resolved_path)

    metadata = {
        "filename": path_obj.name,
        "path": resolved_path,
        "extension": extension,
        "file_size_bytes": file_size,
        "page_count": None
    }

    if extension == ".pdf":
        text, page_count = extract_text_from_pdf(resolved_path)
        metadata["page_count"] = page_count
    elif extension == ".docx":
        text = extract_text_from_docx(resolved_path)
    else:
        # Default text loader for .txt, .md, .py, .json, .csv, etc.
        try:
            with open(resolved_path, "r", encoding="utf-8") as f:
                text = f.read()
        except UnicodeDecodeError:
            with open(resolved_path, "r", encoding="latin-1") as f:
                text = f.read()

    text = text.strip()
    metadata["char_count"] = len(text)
    metadata["word_count"] = len(text.split())

    return text, metadata


def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 150) -> list[str]:
    """
    Split long text into semantically cohesive overlapping chunks.
    Preserves paragraph and sentence boundaries where possible.
    """
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    paragraphs = text.split("\n\n")
    current_chunk = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue

        if len(current_chunk) + len(paragraph) + 2 > chunk_size and current_chunk:
            chunks.append(current_chunk.strip())
            overlap_prefix = current_chunk[-overlap:] if len(current_chunk) > overlap else current_chunk
            current_chunk = overlap_prefix + "\n\n" + paragraph
        else:
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks if chunks else [text]


def get_embedding(text: str) -> list[float]:
    """
    Generate an embedding vector for a single string using Ollama.
    """
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding


def get_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embedding vectors for a list of strings in batch using Ollama.
    """
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]


def main():
    print("=" * 60)
    print("     Document & PDF Vector Embedding Generator")
    print(f"     Model: {EMBEDDING_MODEL}")
    print("=" * 60)

    # Check if a file path was passed as a command-line argument
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        raw_path = sys.argv[1]
        print(f"\nTarget file: {raw_path}")
    else:
        # Look for default sample files to suggest
        default_sample = "Day05(Document_reading)/Data/sample.pdf"
        notes_sample = "Day05(Document_reading)/Data/notes.txt"
        suggested = default_sample if os.path.exists(default_sample) else notes_sample

        print("\nEnter the path to your document or PDF.")
        if os.path.exists(suggested):
            print(f"(Press [Enter] to use default sample: '{suggested}')")

        user_input = input("\nFile path: ").strip()
        raw_path = user_input if user_input else suggested

    # Load and extract text
    try:
        text, metadata = load_document(raw_path)
    except Exception as e:
        print(f"\n[Error loading document]: {e}")
        return

    print("\n--- Document Summary ---")
    print(f"File Name        : {metadata['filename']}")
    print(f"Format           : {metadata['extension'] or 'Plain Text'}")
    print(f"File Size        : {metadata['file_size_bytes'] / 1024:.2f} KB")
    if metadata.get("page_count") is not None:
        print(f"Total Pages      : {metadata['page_count']}")
    print(f"Character Count  : {metadata['char_count']}")
    print(f"Word Count       : {metadata['word_count']}")

    if not text:
        print("\n[Warning] No readable text found in document. If this is a scanned PDF, OCR may be required.")
        return

    # Create chunks if document is large
    chunks = chunk_text(text, chunk_size=1200, overlap=150)
    print(f"Chunks Created   : {len(chunks)}")

    print("\nGenerating embeddings via Ollama...")

    try:
        if len(chunks) == 1:
            embedding = get_embedding(chunks[0])
            embeddings = [embedding]
        else:
            print(f"Processing {len(chunks)} chunks in batch...")
            embeddings = get_embeddings(chunks)

        print("\n--- Embedding Results ---")
        print(f"Total Embeddings : {len(embeddings)}")
        print(f"Vector Dimension : {len(embeddings[0])}")

        # Show sample values from the first embedding
        sample_preview = embeddings[0]
        formatted_preview = ", ".join(f"{val:.4f}" for val in sample_preview)
        print(f"Sample Vector    : {formatted_preview}")

        # Offer saving to JSON file
        save_choice = input("\nSave embeddings to JSON file? (y/N): ").strip().lower()
        if save_choice in ("y", "yes"):
            output_filename = f"{Path(metadata['filename']).stem}_embeddings.json"
            output_data = {
                "metadata": metadata,
                "model": EMBEDDING_MODEL,
                "chunks": [
                    {
                        "chunk_id": idx + 1,
                        "text": chunk,
                        "embedding": emb
                    }
                    for idx, (chunk, emb) in enumerate(zip(chunks, embeddings))
                ]
            }
            with open(output_filename, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2)
            print(f"Embeddings saved successfully to: {output_filename}")

    except Exception as e:
        print(f"\n[Error generating embeddings]: {e}")


if __name__ == "__main__":
    main()
