from pydantic import BaseModel


class WACCInputs(BaseModel):
    risk_free_rate: float
    beta: float
    equity_risk_premium: float
    cost_of_debt: float
    tax_rate: float
    equity_weight: float
    debt_weight: float


def capm_cost_of_equity(rf: float, beta: float, erp: float) -> float:
    return rf + beta * erp


def wacc(inputs: WACCInputs) -> float:
    ke = capm_cost_of_equity(inputs.risk_free_rate, inputs.beta, inputs.equity_risk_premium)
    kd_after_tax = inputs.cost_of_debt * (1 - inputs.tax_rate)
    return inputs.equity_weight * ke + inputs.debt_weight * kd_after_tax


def dcf_value(free_cash_flows: list[float], discount_rate: float, terminal_growth: float) -> float:
    if discount_rate <= terminal_growth:
        raise ValueError("discount_rate must exceed terminal_growth")
    pv = 0.0
    for i, fcf in enumerate(free_cash_flows, start=1):
        pv += fcf / ((1 + discount_rate) ** i)
    tv = free_cash_flows[-1] * (1 + terminal_growth) / (discount_rate - terminal_growth)
    pv += tv / ((1 + discount_rate) ** len(free_cash_flows))
    return pv


def statement_link_check(assets: float, liabilities: float, equity: float, tolerance: float = 1e-6) -> bool:
    return abs(assets - (liabilities + equity)) <= tolerance


def circularity_guard(iterations: int, max_iterations: int = 100) -> bool:
    return iterations <= max_iterations
