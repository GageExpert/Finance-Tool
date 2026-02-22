# Architecture

```text
+---------------------+           +---------------------------+
| Next.js App Router  |  HTTPS    | FastAPI Backend           |
| - Dashboard         +---------->+ - Auth/Watchlists         |
| - Charts (LWC)      |           | - Fundamentals APIs       |
| - Modeling UI       |           | - Valuation/Scenario APIs |
| - Bot UI            |           | - Strategy/Backtest APIs  |
+----------+----------+           +-----------+---------------+
           |                                  |
           |                                  |
           |                      +-----------v-------------+
           |                      | Celery Workers          |
           |                      | - SEC ingestion jobs    |
           |                      | - Model recomputation   |
           |                      +-----------+-------------+
           |                                  |
+----------v----------+             +---------v----------+
| Market Data Adapter |             | Postgres + Redis   |
| (Alpaca MVP)        |             | statements, runs,  |
| swappable providers |             | cache, queue       |
+---------------------+             +--------------------+

External Sources:
- SEC EDGAR submissions/companyfacts (XBRL preferred)
- Alpaca market data + paper trading
```
