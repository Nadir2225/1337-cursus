from .llm_sdk import LLM_Model
from .augmentation import build_prompt
from pathlib import Path
from .search import search_single_query
from .models.MinimalSource import MinimalSource
from .models.MinimalSearchResults import MinimalAnswer
from .models.StudentSearchResults import StudentSearchResultsAndAnswer
from .models.StudentSearchResults import StudentSearchResults
import json


def generate_answer(query: str, llm: LLM_Model, k: int, sources: list[MinimalSource] | None = None) -> str:
    if not sources:
        prompt = build_prompt(query, k)
    else:
        prompt = build_prompt(query, k, sources)
    template_prompt = llm.build_template(prompt)
    tokenized_prompt = llm.encode(template_prompt)

    generated = llm.generate(tokenized_prompt, 500)

    prompt_length = len(tokenized_prompt[0])
    tokenized_answer = generated[:, prompt_length:]

    answer = llm.decode(tokenized_answer)

    return answer

def answer(query: str, k: int) -> str:
    if k == 0:
        raise ValueError("[ERROR]: k must be larger than 0")
    if not query:
        raise ValueError("[ERROR]: no query detected!")
    llm = LLM_Model("Qwen/Qwen3-0.6B")

    answer = generate_answer(query, llm, k)

    return answer

def answer_dataset(student_search_results_path: str, save_dir: str):
    llm = LLM_Model("Qwen/Qwen3-0.6B")

    try:
        with open(student_search_results_path, "r") as f:
            data = json.load(f)
        res = StudentSearchResults(**data)
    except:
        raise Exception("Error (File not found or wrong file format): please search_dataset before using the answer_dataset command")
    
    results = res.search_results
    k = res.k

    print(f"Loaded {len(results)} questions ... ", end='')

    min_search_res: list[MinimalAnswer] = []
    processed = 0
    for i, result in enumerate(results, start=1):
        try:
            this_answer = generate_answer(result.question, llm, k, result.retrieved_sources)
            min_search_res.append(
                MinimalAnswer(
                    question_id=result.question_id,
                    question=result.question,
                    answer=this_answer,
                    retrieved_sources=result.retrieved_sources,
                )
            )
        except:
            continue
        processed += 1
        if i == 2:
                break

    print(f"Processed {processed} of {len(results)} questions")

    search_results = StudentSearchResultsAndAnswer(
        search_results=min_search_res,
        k=k
    )

    save_directory = Path(save_dir) / "StudentSearchResultsAndAnswer.json"

    save_directory.parent.mkdir(parents=True, exist_ok=True)

    with open(save_directory, "w") as f:
        json.dump(
            search_results.model_dump(),
            f,
            indent=2
        )

    print(f"Saved student_search_results_and_answer to {save_directory}")
