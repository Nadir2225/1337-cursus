import json
from pathlib import Path
import bm25s
from .models.MinimalSource import MinimalSource
from .models.MinimalSearchResults import MinimalSearchResults


def search_single_query(query: str, k: int) -> list[MinimalSource]:
    processed_path = Path("data/processed")

    retriver = bm25s.BM25.load(processed_path, load_corpus=True)

    query_tokens = bm25s.tokenize(query, stopwords='en')

    results = retriver.retrieve(query_tokens, k=k)

    final_results = []
    for r in results[0][0]:
        final_results.append(MinimalSource.model_validate(r))

    return final_results
        

def search_dataset(dataset_path: str, k: int, save_directory):
    with open(dataset_path, "r") as f:
        data = json.load(f)

    search_results: list[MinimalSearchResults] = []
    for question in data["rag_questions"]:
        search_results.append(
            MinimalSearchResults(
                question_id=question["question_id"],
                question=question["question"],
                retrieved_sources=search_single_query(question["question"], k),
            )
        )

    save_directory = Path(save_directory)

    save_directory.parent.mkdir(parents=True, exist_ok=True)

    with open(save_directory, "w") as f:
        json.dump(
            [r.model_dump() for r in search_results],
            f,
            indent=2
        )