from typing import Any

import httpx

from app.core.config import settings

SEC_BASE = "https://data.sec.gov"


class EdgarClient:
    def __init__(self) -> None:
        self.headers = {"User-Agent": settings.sec_user_agent, "Accept-Encoding": "gzip, deflate"}

    async def get_submissions(self, cik: str) -> dict[str, Any]:
        url = f"{SEC_BASE}/submissions/CIK{cik.zfill(10)}.json"
        async with httpx.AsyncClient(timeout=20) as client:
            resp = await client.get(url, headers=self.headers)
            resp.raise_for_status()
            return resp.json()

    async def get_company_facts(self, cik: str) -> dict[str, Any]:
        url = f"{SEC_BASE}/api/xbrl/companyfacts/CIK{cik.zfill(10)}.json"
        async with httpx.AsyncClient(timeout=20) as client:
            resp = await client.get(url, headers=self.headers)
            resp.raise_for_status()
            return resp.json()
