from dateutil.relativedelta import relativedelta
import decimal

from app.schemas import DepositIn


def calculate_amount_over_period(deposit: DepositIn) -> dict[str, decimal.Decimal]:
    result = {}
    amount = deposit.amount
    for i in range(deposit.periods):
        new_date = (deposit.date + relativedelta(months=i)).strftime('%d.%m.%Y')
        amount *= ((100 + deposit.rate / 12) / 100)
        result[new_date] = amount.quantize(decimal.Decimal('1.00'), decimal.ROUND_HALF_UP).normalize()
    return result
