from .models.functions_definitions import Functiondefinition
from .models.prompts import Prompt
import json
from llm_sdk import Small_LLM_Model


def load_functions(functions_definition_path: str) -> list[Functiondefinition]:
    """Read the function definitions JSON file and validate it."""
    loaded_functions = []
    with open(functions_definition_path, "r") as f:
        functions = json.load(f)
    for function in functions:
        loaded_functions.append(Functiondefinition(**function))
    return loaded_functions


def load_prompts(prompts_path: str) -> list[Prompt]:
    """Read the test prompts JSON file and validate it."""
    loaded_prompts = []
    with open(prompts_path, "r") as f:
        prompts = json.load(f)
    for prompt in prompts:
        loaded_prompts.append(Prompt(**prompt))
    return loaded_prompts


def load_vocabulary(model: Small_LLM_Model) -> dict[str, int]:
    """Return the model tokenizer vocabulary as a token string to id map."""
    vocab_path = model.get_path_to_tokenizer_file()
    with open(vocab_path, "r", encoding="utf-8") as f:
        tok_data = json.load(f)
    raw_data: dict[str, int] = tok_data.get("model", {}).get("vocab", {})
    return raw_data
