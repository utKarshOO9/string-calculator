from fastapi import FastAPI
from api.model import CalculatorRequest, CalculatorResponse
from string_calculator import calculator as calc

api = FastAPI()


@api.post("/calculator", response_model=CalculatorResponse)
async def calculator(req: CalculatorRequest):
    result = calc.add(req.numbers)
    return CalculatorResponse(input=req.numbers, output=result, errors=[])