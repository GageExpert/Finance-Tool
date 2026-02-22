from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.sql import func

from app.db.session import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Watchlist(Base):
    __tablename__ = "watchlists"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)


class WatchlistItem(Base):
    __tablename__ = "watchlist_items"
    id = Column(Integer, primary_key=True)
    watchlist_id = Column(Integer, ForeignKey("watchlists.id"), nullable=False)
    ticker = Column(String(16), nullable=False)


class Filing(Base):
    __tablename__ = "filings"
    id = Column(Integer, primary_key=True)
    ticker = Column(String(16), index=True)
    accession = Column(String(32), nullable=False)
    filing_type = Column(String(16), default="10-K")
    filing_date = Column(String(16))
    source = Column(String(32), default="sec_xbrl")
    raw_payload = Column(JSON)


class StatementLine(Base):
    __tablename__ = "statement_lines"
    id = Column(Integer, primary_key=True)
    filing_id = Column(Integer, ForeignKey("filings.id"), nullable=False)
    statement = Column(String(32), nullable=False)
    line_order = Column(Integer, nullable=False)
    tag = Column(String(128), nullable=False)
    label = Column(String(255), nullable=False)
    value = Column(Float)
    period = Column(String(32), nullable=False)
    is_user_mapped = Column(Boolean, default=False)


class StrategyRun(Base):
    __tablename__ = "strategy_runs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    config = Column(JSON, nullable=False)
    metrics = Column(JSON)
    logs = Column(JSON)


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ticker = Column(String(16), nullable=False)
    content = Column(Text, default="")
