import datetime

from pydantic import BaseModel

class BinsData(BaseModel):
    card_id: str
    bin_id: int
    bin_type: str
    timestamp: datetime.datetime
    weight: int
    recycle_status_ok: bool = False