# Axium

Production-oriented full-stack scaffold for fundamentals + technical analysis + paper bot workflows.

## Stack
- Frontend: Next.js App Router, TypeScript, Tailwind, Lightweight Charts
- Backend: FastAPI, SQLAlchemy, Celery, Redis
- DB: Postgres
- Data: SEC EDGAR XBRL endpoints (`submissions`, `companyfacts`) with descriptive `User-Agent`

## Deliverables Included
1. PRD: `docs/PRD.md`
2. Architecture: `docs/ARCHITECTURE.md`
3. Runnable skeleton with Docker Compose
4. Core API flows:
   - Auth/signup/login
   - Watchlist create + ticker add
   - Chart analysis endpoint + frontend chart panel
   - SEC ingestion endpoint storing filing payload
   - DCF/WACC finance math endpoints
   - Strategy parse + backtest endpoints
5. Demo data: `seed/demo_data.json`

## Quickstart
```bash
cp .env.example .env
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend docs: http://localhost:8000/docs

## Local backend test
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Env vars
See `.env.example`.

## Security and Risk Notes
- Keep broker/API keys server-side only; do not expose secrets to client.
- Encrypt API keys at rest before production use (KMS/Vault recommended).
- Live trading is intentionally disabled by default in MVP.
- AI outputs are feature-based explanations, not guarantees or investment advice.

## Limitations (MVP)
- PDF parsing and user mapping UI are planned; SEC XBRL path is primary and implemented first.
- Backtesting is simplified and does not yet include robust walk-forward simulation.
