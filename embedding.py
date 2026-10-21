# Simple demo for generating a text embedding with Google EmbeddingGemma-2 (740M)
# Ensure required packages are installed in your virtual environment:
# uv pip install torch transformers

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def get_embedding(text: str):
    response = client.embeddings.create(
        model=os.getenv("EMBEDDING_MODEL"),
        input=text
    )
    return response.data[0].embedding

if __name__ == "__main__":
    demo_text = """
    Artificial Intelligence agents represent a significant paradigm shift from traditional rule-based 
    software to autonomous, goal-driven systems capable of reasoning, planning, and tool use. At the core 
    of modern agent architectures lies the synergy between Large Language Models (LLMs), high-dimensional 
    vector embeddings, and persistent memory stores.

    Vector embeddings transform unstructured textual information—such as documents, user queries, code 
    snippets, and conversational history—into dense numerical representations in a continuous geometric space. 
    In this embedding space, semantic similarity is preserved as spatial proximity: concepts with related 
    meanings cluster closely together, irrespective of syntactic variation or specific vocabulary choices. 

    When integrated into Retrieval-Augmented Generation (RAG) pipelines, embedding models like EmbeddingGemma-2 
    allow autonomous agents to overcome finite context window limitations. By segmenting extensive corpora 
    into modular passages, indexing their vector representations in a vector database, and executing nearest-neighbor 
    searches (such as cosine similarity or dot product metrics), agents can dynamically retrieve relevant factual 
    knowledge in real time to ground their reasoning and mitigate hallucinations.
    """.strip()

    print(f"Text Character Count : {len(demo_text)}")
    print(f"Text Word Count      : {len(demo_text.split())}")
    print("\nGenerating embedding via Ollama...")

    embedding = get_embedding(demo_text)

    print(f"Embedding Dimensions : {len(embedding)}")
    print(f"Embeddings           : {embedding}")

