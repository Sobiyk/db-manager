import asynctnt

from app.core.config import settings

conn = asynctnt.Connection(host=settings.tnt_host, port=settings.tnt_port)
