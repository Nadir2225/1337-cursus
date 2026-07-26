*This project has been created as part of the 42 curriculum by nel-ouad.*

# call me maybe

## Description

A function calling tool: it turns natural language prompts into structured
function calls, using the small `Qwen/Qwen3-0.6B` model.

Instead of answering *"What is the sum of 2 and 3?"* with `5`, it answers with
the call to make:

```json
{ "prompt": "What is the sum of 2 and 3?", "name": "fn_add_numbers", "parameters": {"a": 2, "b": 3} }
```

The JSON is never "hoped for": it is produced by **constrained decoding**, so
the output is always parseable.

## Instructions

```bash
make install          # uv sync
make run              # uv run python3 -m src
make debug            # run under pdb
make lint             # flake8 + mypy
make clean            # remove __pycache__ / .mypy_cache
```

(the `Makefile` is in `src/`)

Or directly:

```bash
uv run python -m src \
  --functoins_definition data/input/functions_definition.json \
  --input data/input/function_calling_tests.json \
  --output data/output/functions_results.json \
  --model Qwen/Qwen3-0.6B
```

All arguments are optional; the values above are the defaults.

## Algorithm

1. **Load** the function definitions and the prompts, validated with
   **pydantic** models (`Functiondefinition`, `Prompt`).
2. **Build a system prompt** listing every available function with its
   parameters and description, plus the rule: if nothing matches, return
   `name: "none"`.
3. **Load the vocabulary** from the tokenizer file
   (`get_path_to_tokenizer_file()`) to map tokens to their string form.
4. **Filter the vocabulary** (`build_json_valid`) keeping only tokens made of
   characters that can appear inside our JSON (letters, digits, `{}`, `"`, `,`,
   `:`, ...). Every other token is excluded from the start.
5. **Force the beginning** of the answer with `{"name": "` so the model can only
   continue an already-started JSON object.
6. **Generate token by token**: ask the model for logits, then
   `get_best_valid_id` picks the highest logit **among the allowed token ids
   only** — the equivalent of setting every other logit to `-inf`.
7. **Stop** when the braces are balanced (`closed_dict`), i.e. the JSON object
   is closed.
8. **Save** all results as a JSON array in `data/output/`.

## Design decisions

- **Character-level whitelist** instead of a full JSON grammar: much simpler,
  and enough to keep generation inside the JSON alphabet.
- **Prefix forcing** (`{"name": "`): removes the hardest part for a 0.6B model,
  which is starting the structure correctly.
- **Brace counting** as the stop condition: no need for an EOS token, no
  trailing prose.
- **Function choice made by the model**, never by keyword matching — the system
  prompt only describes the functions.
- **pydantic everywhere** for input validation, so a malformed input file fails
  with a clear message instead of a crash.
- **rich** for readable progress output during generation.

## Performance

- **Valid JSON:** 100% — decoding cannot produce anything else.
- **Accuracy:** good on the provided test set; the remaining errors are
  function selection on ambiguous prompts, not malformed output.
- **Speed:** one forward pass per generated token, so runtime scales with the
  number of prompts × answer length. The whole provided test file runs in a few
  minutes on CPU (the elapsed time is printed at the end).
- **Reliability:** missing files, invalid JSON, schema errors and Ctrl-C are all
  caught and reported with a clear message.

## Testing

- Ran the provided `function_calling_tests.json` and checked every entry:
  correct function, correct parameter names and types.
- Edge cases: empty strings, big numbers, quotes and special characters inside
  prompts, prompts matching no function (`"none"`).
- `make lint` (flake8 + mypy) passes.

## Resources

- [Qwen3 model card](https://huggingface.co/Qwen/Qwen3-0.6B)

### AI usage

AI was used as a helper, not as the author:

- To explain constrained decoding and how logit masking works.
- To help debug the token filtering (special `Ġ` / `Ċ` markers).
- To rephrase and format this README.

The implementation, the decoding logic and the design choices were written and
are fully understood by me.
