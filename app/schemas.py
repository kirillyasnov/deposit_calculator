import datetime
from decimal import Decimal

from pydantic import BaseModel, Field, validator


class DepositIn(BaseModel):
    date: datetime.datetime
    periods: int = Field(ge=1, le=60)
    amount: Decimal = Field(ge=10000, le=3_000_000)
    rate: Decimal = Field(ge=1, le=8)

    @validator('date', pre=True)
    def parse_date(cls, v):
        return datetime.datetime.strptime(v, '%d.%m.%Y')
