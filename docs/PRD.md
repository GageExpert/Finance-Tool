# Axium PRD (MVP)

## Product Goal
Axium combines institutional-grade fundamental modeling with TradingView-style technical charting and risk-controlled paper trading workflows.

## Users
- Fundamental analysts
- Swing traders/options traders
- PMs managing watchlists and reusable workspaces

## Core Jobs-to-be-Done
1. Ingest 10-K data and normalize 3 statements over 5 years.
2. Build and edit driver-based forecasts and valuation outputs.
3. Analyze charts with indicators + AI feature reasoning.
4. Create/validate strategy rules, backtest, and paper execute.

## MVP Scope
- Auth + watchlists + notes + demo mode
- SEC XBRL ingestion using submissions + companyfacts endpoints
- Statement normalization tables + editable mappings
- DCF/WACC/comps/scenarios with sensitivity matrices
- Lightweight Charts-based charting and indicator templates
- AI chart analysis from computed features (no certainty claims)
- Strategy builder -> config -> backtest -> paper execution logs

## Non-Functional Requirements
- Minimal accessible UI
- Secrets server-side only, encrypted at rest
- Background jobs for ingestion/recompute
- Cache/rate-limit external APIs
- Data source transparency for all AI outputs

## Risk/Compliance
- SEC fair access: descriptive User-Agent and respectful request cadence
- Live trading disabled by default with explicit enablement gate + kill switch
- No investment advice guarantees
