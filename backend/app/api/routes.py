from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.db.session import Base, engine, get_db
from app.models.entities import Filing, User, Watchlist, WatchlistItem
from app.schemas.common import Token, UserCreate
from app.services.chart_ai import analyze_features
from app.services.edgar import EdgarClient
from app.services.finance_math import WACCInputs, dcf_value, wacc
from app.services.strategy import backtest, parse_strategy

router = APIRouter()
Base.metadata.create_all(bind=engine)


@router.post("/auth/signup", response_model=Token)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    user = User(email=payload.email, hashed_password=hash_password(payload.password))
    db.add(user)
    db.commit()
    return Token(access_token=create_access_token(payload.email))


@router.post("/auth/login", response_model=Token)
def login(payload: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return Token(access_token=create_access_token(payload.email))


@router.post("/watchlists")
def create_watchlist(name: str, user_id: int, db: Session = Depends(get_db)):
    wl = Watchlist(name=name, user_id=user_id)
    db.add(wl)
    db.commit()
    db.refresh(wl)
    return wl


@router.post("/watchlists/{watchlist_id}/items")
def add_ticker(watchlist_id: int, ticker: str, db: Session = Depends(get_db)):
    item = WatchlistItem(watchlist_id=watchlist_id, ticker=ticker.upper())
    db.add(item)
    db.commit()
    return {"ok": True}


@router.get("/analysis/chart")
def chart_analysis():
    demo_features = {"closes": [100 + i for i in range(30)], "atr": 2.1, "rsi": 61, "volume_trend": "rising"}
    return analyze_features(demo_features)


@router.get("/fundamentals/ingest/{cik}")
async def ingest_sec(cik: str, db: Session = Depends(get_db)):
    client = EdgarClient()
    sub = await client.get_submissions(cik)
    facts = await client.get_company_facts(cik)
    recent = sub.get("filings", {}).get("recent", {})
    accession = (recent.get("accessionNumber") or ["unknown"])[0]
    filing = Filing(ticker=sub.get("tickers", ["UNK"])[0], accession=accession, raw_payload={"sub": sub, "facts": facts})
    db.add(filing)
    db.commit()
    return {"filing_id": filing.id, "ticker": filing.ticker, "warning": "PDF parsing less accurate; edit mappings if upload used."}


@router.post("/valuation/dcf")
def valuation_endpoint(cash_flows: list[float], discount_rate: float, terminal_growth: float):
    return {"enterprise_value": dcf_value(cash_flows, discount_rate, terminal_growth)}


@router.post("/valuation/wacc")
def wacc_endpoint(inputs: WACCInputs):
    return {"wacc": wacc(inputs)}


@router.post("/bot/strategy")
def strategy_from_prompt(prompt: str):
    return parse_strategy(prompt)


@router.post("/bot/backtest")
def run_backtest(prices: list[float]):
    return backtest(prices)
