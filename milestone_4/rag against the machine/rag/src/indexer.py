from pathlib import Path
import bm25s
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from .models.MinimalSource import MinimalSource
from tqdm import tqdm

BAR_FORMAT = (
    "{desc:<12}{percentage:3.0f}%|{bar:10}| {n_fmt}/{total_fmt}"
    " [{elapsed}<{remaining}, {rate_int} {unit}/s]"
)

class Progress(tqdm):

    @property
    def format_dict(self):
        d = super().format_dict
        rate = d["rate"] or (d["n"] / d["elapsed"] if d["elapsed"] else 0)
        d["rate_int"] = f"{rate:.0f}"
        return d


    def progress(iterable, desc: str, unit: str, total: int | None = None):
        return Progress(
            iterable,
            desc=desc,
            unit=unit,
            total=total,
            ascii=True,
            bar_format=BAR_FORMAT
        )


def chunker(file_path: Path, max_size: int) -> tuple[list[str], list[MinimalSource]]:
    lang = None
    if file_path.suffix == ".py":
        lang = Language.PYTHON
    elif file_path.suffix == ".md":
        lang = Language.MARKDOWN
    elif file_path.suffix == ".txt":
        lang = Language.MARKDOWN
    else:
        raise Exception("chunking error: wrong file extension")
    if max_size <= 0:
        raise ValueError("[ERROR] max_size is less or equal to 0")

    with open(file_path, "r") as f:
        text = f.read()
        if not text:
            return [], []
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=lang,
            chunk_size=max_size,
            chunk_overlap=min(100, max_size // 5),
            add_start_index=True
        )
        docs = splitter.create_documents([text])
        chunks = []
        texts = []
        for doc in docs:
            last_index = doc.metadata["start_index"] + len(doc.page_content)
            chunks.append(
                MinimalSource(
                    file_path=str(file_path),
                    first_character_index=doc.metadata["start_index"],
                    last_character_index=last_index
                )
            )
            texts.append(doc.page_content)
        
        return texts, chunks

def eligible_file(path: Path):
    valid_ext = path.suffix in (".py", ".md", ".txt")
    return path.is_file() and valid_ext

def indexer(max_size: int):
    raw_path = Path("data/raw/vllm-0.10.1")
    processed_path = Path("data/processed")

    files = [path for path in raw_path.rglob("*") if eligible_file(path)]
    chunks: list[MinimalSource] = []
    texts: list[str] = []
    for file in Progress.progress(files, "Chunking: ", "file"):
        new_text, new_chunks = chunker(file, max_size)
        chunks += new_chunks
        texts += new_text

    corpus_tokens = bm25s.tokenize(
        Progress.progress(texts, "Tokenizing: ", "chunk"),
        stopwords=None,
        show_progress=False
    )

    retriver = bm25s.BM25()

    retriver.index(corpus_tokens, show_progress=False)

    retriver.save(
        processed_path,
        corpus=[chunk.model_dump() for chunk in chunks]
    )

    print(f"Ingestion complete! Indices saved under {processed_path}/")
    