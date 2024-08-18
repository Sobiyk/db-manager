import asynctnt

from app.core.config import settings

conn = asynctnt.Connection(port=settings.tnt_port)
