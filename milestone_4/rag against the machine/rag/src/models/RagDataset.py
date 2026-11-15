from pydantic import BaseModel
from .Question import AnsweredQuestion, UnansweredQuestion


class RagDataset(BaseModel):
    rag_questions: list[AnsweredQuestion | UnansweredQuestion]