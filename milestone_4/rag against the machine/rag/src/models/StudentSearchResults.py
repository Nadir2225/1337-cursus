from pydantic import BaseModel
from .MinimalSearchResults import MinimalAnswer, MinimalSearchResults



class StudentSearchResults(BaseModel):
    search_results: list[MinimalSearchResults]
    k: int


class StudentSearchResultsAndAnswer(BaseModel):
    search_results: list[MinimalAnswer]
    k: int