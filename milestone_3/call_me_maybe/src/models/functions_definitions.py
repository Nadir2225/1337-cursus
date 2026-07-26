from pydantic import BaseModel


class Parameter(BaseModel):
    """A single function parameter, described by its JSON type."""

    type: str


class ReturnType(BaseModel):
    """What a function gives back, described by its JSON type."""

    type: str


class Functiondefinition(BaseModel):
    """One callable function as declared in functions_definition.json."""

    name: str
    description: str
    parameters: dict[str, Parameter]
    returns: ReturnType
