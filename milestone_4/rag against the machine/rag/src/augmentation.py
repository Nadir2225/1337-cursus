from .search import search_single_query
from .models.MinimalSource import MinimalSource



SYSTEM_RULES = [
    "You are a question-answering assistant for the vLLM codebase.\n",
    "Answer questions using ONLY the provided sources.\n",
    "Do not use outside knowledge or invent information.\n",
    "\n",

    "RULES:\n",
    "1. Read all provided sources before answering.\n",
    "2. Identify which source or sources contain information relevant to the question.\n",
    "3. Answer the exact question. Do not give unrelated information.\n",
    "4. Prefer precise and complete answers over general explanations.\n",
    "5. Preserve technical details exactly as written in the sources:\n",
    "   - Commands and their arguments\n",
    "   - Flags and parameter names\n",
    "   - Function and class names\n",
    "   - File paths\n",
    "   - Values, versions, and numbers\n",
    "6. NEVER invent missing arguments, flags, values, or commands.\n",
    "7. Do not replace a specific answer with a vague explanation.\n",
    "8. If a source contains an exact command that answers the question,\n",
    "   reproduce the complete command, including all its arguments.\n",
    "9. If the question asks for a command, put the command in a code block.\n",
    "10. If multiple sources contain relevant information, combine them\n",
    "    only when they are compatible and answer the same question.\n",
    "11. Cite every source used with its corresponding source number,\n",
    "    for example [Source 1]. Do not cite unused sources.\n",
    "\n",

    "ANSWERING PARTIAL QUESTIONS:\n",
    "If the sources answer only part of the question, provide the\n",
    "supported information and clearly state what is not specified.\n",
    "Do not guess to fill missing information.\n",
    "\n",

    "WHEN INFORMATION IS NOT AVAILABLE:\n",
    "If none of the sources contains information that answers any part\n",
    "of the question, respond with exactly:\n",
    "I could not find the answer in the provided sources.\n",
    "\n",

    "OUTPUT:\n",
    "Be concise, direct, and technically accurate.\n",
    "Do not explain your reasoning.\n",
    "Do not repeat the source file paths.\n",
    "Never append the fallback sentence to an answer that contains\n",
    "relevant information.\n",
]

END_PROMPT = [
    "\n",
    "Now answer the question using the sources above.\n",
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

def build_user_message(query: str, sources: list[MinimalSource]) -> str:
    parts = ["Sources\n"]
    for i, source in enumerate(sources, start=1):
        content = read_minimal_source(source)
        parts.append(f"[Source {i}] {source.file_path}\n{content}\n\n")

    parts.append(f"Question: {query}\n")
    parts.extend(END_PROMPT)

    return "".join(parts)


def build_prompt(query: str, k: int, sources: list[MinimalSource] | None = None) -> list[dict[str, str]]:
    if not sources:
        sources = search_single_query(query, k)

    return [
        {"role": "system", "content": "".join(SYSTEM_RULES)},
        {"role": "user", "content": build_user_message(query, sources)}
    ]