from celery import Celery

from app.core.config import settings

celery = Celery("axium", broker=settings.redis_url, backend=settings.redis_url)


@celery.task
def recompute_model_task(model_id: int):
    return {"model_id": model_id, "status": "recomputed"}
