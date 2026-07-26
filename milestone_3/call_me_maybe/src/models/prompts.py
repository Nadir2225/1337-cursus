from pydantic import BaseModel


class Prompt(BaseModel):
    """A natural language prompt to translate into a function call."""

    prompt: str
