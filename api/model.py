from typing import List
from pydantic import BaseModel


class CalculatorRequest(BaseModel):
    numbers: str


class CalculatorResponse(BaseModel):
    input: str
    output: int | None
    errors: List[str]