import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.schemas import DepositIn
from app.utils import calculate_amount_over_period


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=400, content={'error': str(exc)})


@app.post('/deposits')
async def calculate_deposit(deposit: DepositIn):
    return calculate_amount_over_period(deposit)


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=80, reload=True)
