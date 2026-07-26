from typing import Optional
from .models.functions_definitions import Functiondefinition


def build_system_prompt(functions: Functiondefinition) -> str:
    """Build the system prompt listing every function the model may call."""
    system_prompts = [
        (
            'STRICT SYSTEM RULE: Use ONLY a '
            'matching function from the list below.'
        ),
        'If NO function matches the user\'s intent (even if types match), '
        'set name: "none" and parameters: {}.',
        'Never use an unrelated function for a different task.',
        '',
        'RULES:',
        '-the word "run" MEANS "execute"',
        'Available functions:',
    ]
    for function in functions:
        params = ', '.join(
            f"{param_name}: {param.type}"
            for param_name, param in function.parameters.items()
        )
        system_prompts.append(
            f"  -{function.name}({params}): {function.description}"
        )
    system_prompts.append(
        '\nOutput ONLY valid JSON: {"name": "<fn>", "parameters": {<args>}}'
    )
    return "\n".join(system_prompts)


def build_json_valid(vocab: dict) -> set[int]:
    """Keep only the token ids made of characters allowed inside our JSON."""
    valid_set = set(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        "0123456789*_./\\'!?()[-]{}ĠĊġċ"
        '",:'
    )
    valid_vocab = set()
    for token_str, token_id in vocab.items():
        if token_str and all(c in valid_set for c in token_str):
            valid_vocab.add(token_id)
    return valid_vocab


def get_best_valid_id(logits: list, valid_ids: list) -> Optional[int]:
    """Return the highest scoring allowed token id, None if there is none."""
    max = logits[0]
    max_id = 0
    found = False
    for id, logit in enumerate(logits):
        if (logit > max) and (id in valid_ids):
            max = logit
            max_id = id
            found = True
    if found:
        return max_id
    else:
        return None


def closed_dict(raw: str) -> bool:
    """Tell whether every brace opened in *raw* has been closed again."""
    open = 0
    for c in raw:
        if c == '{':
            open += 1
        if c == '}':
            open -= 1
    return (open == 0)


def fix_type(obj: dict, functions: list[Functiondefinition]) -> None:
    """Cast the generated parameters in place to the declared numeric types."""
    for function in functions:
        if obj.get("name") == function.name:
            for param_name, param in function.parameters.items():
                if param_name in obj["parameters"]:
                    if param.type == "number":
                        obj["parameters"][param_name] = float(
                            obj["parameters"][param_name]
                        )
                    elif param.type == "integer":
                        obj["parameters"][param_name] = int(
                            obj["parameters"][param_name]
                        )
