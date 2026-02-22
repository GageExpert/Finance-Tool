import pytest

from app.services.finance_math import WACCInputs, circularity_guard, dcf_value, statement_link_check, wacc


def test_wacc_basic():
    inputs = WACCInputs(
        risk_free_rate=0.04,
        beta=1.1,
        equity_risk_premium=0.05,
        cost_of_debt=0.06,
        tax_rate=0.21,
        equity_weight=0.7,
        debt_weight=0.3,
    )
    assert round(wacc(inputs), 4) == 0.0827


def test_dcf_positive_value():
    val = dcf_value([100, 110, 121], 0.1, 0.03)
    assert val > 1000


def test_dcf_invalid_growth():
    with pytest.raises(ValueError):
        dcf_value([100], 0.02, 0.03)


def test_statement_link_check():
    assert statement_link_check(100, 60, 40)
    assert not statement_link_check(100, 50, 40)


def test_circularity_guard():
    assert circularity_guard(50)
    assert not circularity_guard(101)
