from fastapi import FastAPI
from api.model import CalculatorRequest, CalculatorResponse

api = FastAPI()


@api.post("/calculator", response_model=CalculatorResponse)
async def calculator(req: CalculatorRequest):
    return CalculatorResponse(input=req.numbers, output=0, errors=[])