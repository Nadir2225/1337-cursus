from .search import search_single_query
from .models.MinimalSource import MinimalSource


SYSTEM_RULES = [
    "You answer questions about the vLLM codebase using only the ",
    "sources you are given.\n",
    "Each source is a piece of documentation or Python code, ",
    "shown with its file path.\n",
    "\n",
    "How to answer:\n",
    "1. Find the parts of the sources that answer the question.\n",
    "2. Answer in a few short sentences, using the wording of the ",
    "sources.\n",
    "3. Copy commands, flags, function names and class names ",
    "exactly as written.\n",
    "4. If the sources only answer part of the question, give that ",
    "part.\n",
    "5. End with the number of the source you used, like [Source 2].\n",
    "\n",
    "If none of the sources answers any part of the question, ",
    "write only this sentence:\n",
    "I could not find the answer in the provided sources.\n",
    "\n",
    "Example 1:\n",
    "[Source 1] data/raw/example/docs/thumbnails.md\n",
    "Thumbnails are resized to 256 pixels. ",
    "Use --thumb-size to change it.\n",
    "Question: How do I change the thumbnail size?\n",
    "Answer: Use the --thumb-size option. By default, thumbnails ",
    "are 256 pixels. [Source 1]\n",
    "\n",
    "Example 2:\n",
    "[Source 1] data/raw/example/docs/thumbnails.md\n",
    "Thumbnails are resized to 256 pixels. ",
    "Use --thumb-size to change it.\n",
    "Question: What is the capital of France?\n",
    "Answer: I could not find the answer in the provided sources.\n",
]

END_PROMPT = [
    "\n",
    "Answer using only the sources above. ",
    "If none of them answers any part of the question, write: ",
    "I could not find the answer in the provided sources.",
]

def read_minimal_source(source: MinimalSource) -> str:
    content = ""
    try:
        with open(source.file_path, "r") as file:
            content = file.read()
    except:
        return content

    first = source.first_character_index
    last = source.last_character_index
    return content[first:last]

def build_user_message(query: str, sources: int) -> str:
    parts = ["Sources\n"]
    for i, source in enumerate(sources):
        content = read_minimal_source(source)
        parts.append(f"[Source {i}] {source.file_path}\n{content}\n\n")

    parts.append(f"Question: {query}\n")
    parts.extend(END_PROMPT)

    return "".join(parts)


def build_prompt(query: str, k: int) -> list[dict[str, str]]:
    sources = search_single_query(query, k)

    return [
        {"role": "system", "content": "".join(SYSTEM_RULES)},
        {"role": "user", "content": build_user_message(query, sources)}
    ]