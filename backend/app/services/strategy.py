from dataclasses import dataclass


@dataclass
class StrategyConfig:
    timeframe: str
    signal: str
    max_positions: int
    max_daily_loss: float


def parse_strategy(prompt: str) -> dict:
    return {
        "timeframe": "1D" if "daily" in prompt.lower() else "1h",
        "universe": ["AAPL", "MSFT"],
        "signal": "ma_crossover",
        "risk": {"max_drawdown": 0.1, "max_daily_loss": 0.02, "max_positions": 5},
        "slippage_bps": 5,
    }


def backtest(prices: list[float]) -> dict:
    if len(prices) < 3:
        return {"return": 0.0, "trades": []}
    ret = (prices[-1] - prices[0]) / prices[0]
    return {"return": ret, "trades": [{"side": "buy", "price": prices[0]}, {"side": "sell", "price": prices[-1]}]}
