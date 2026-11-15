from .llm_sdk import LLM_Model
from .augmentation import build_prompt


def generate_answer(query: str, llm: LLM_Model, k: int) -> str:
    prompt = build_prompt(query, k)
    template_prompt = llm.build_template(prompt)
    tokenized_prompt = llm.encode(template_prompt)
    tokenized_answer = llm.generate(tokenized_prompt, 500)
    answer = llm.decode(tokenized_answer)[0][:len(tokenized_prompt[0])]
    return answer

def answer(query: str, k: int):
    if k == 0:
        raise ValueError("[ERROR]: k must be larger than 0")
    if not query:
        raise ValueError("[ERROR]: no query detected!")
    llm = LLM_Model("Qwen/Qwen3-0.6B")

    answer = generate_answer(query, llm, k)

    print(answer)