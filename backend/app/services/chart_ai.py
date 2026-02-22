from statistics import mean


def analyze_features(features: dict) -> dict:
    closes = features.get("closes", [])
    atr = features.get("atr", 0)
    rsi = features.get("rsi", 50)
    volume_trend = features.get("volume_trend", "flat")

    trend = "uptrend" if closes and closes[-1] > mean(closes[-20:]) else "downtrend"
    momentum = "overbought" if rsi > 70 else "oversold" if rsi < 30 else "neutral"

    thesis = (
        f"Feature-based read: {trend}, momentum {momentum}, ATR {atr:.2f}, volume {volume_trend}. "
        "This is a probabilistic 1-2 week idea, not a guarantee."
    )

    return {
        "thesis": thesis,
        "risk_plan": {
            "entry": "Break of recent high/low with confirmation",
            "stop": "1.5x ATR beyond invalidation",
            "targets": ["1R", "2R", "trail at 20 EMA"],
        },
        "options_templates": ["debit spread", "calendar", "vertical"],
        "assumptions": ["Uses computed indicators only", "No certainty claimed"],
        "data_sources": ["OHLCV bars", "computed ATR/RSI/MA"],
    }
