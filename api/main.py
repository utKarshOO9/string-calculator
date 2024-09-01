from fastapi import FastAPI
from api.model import CalculatorRequest, CalculatorResponse
from string_calculator import calculator as calc

api = FastAPI()


@api.post("/calculator", response_model=CalculatorResponse)
async def calculator(req: CalculatorRequest):
    errors = []
    result = None
    try:
        result = calc.add(req.numbers)
    except calc.NegativeNumberError as e:
        errors.append(str(e))
    return CalculatorResponse(input=req.numbers, output=result, errors=errors)