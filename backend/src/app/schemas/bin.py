import datetime

from pydantic import BaseModel

class BinsOpened(BaseModel):
    card_id: str
    bin_id: int
    bin_type: str
    timestamp: datetime.datetime
    weight: int
    recycle_status_ok: bool = False


class BinsStatus(BaseModel):
    bin_id: int
    timestamp: datetime.datetime
    waste_status: int




