from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import schemas, models
from app.api import deps
from typing import List

from app.schemas.user_bins_data import BinsData

import os
import pymongo

MONGODB_URI = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(MONGODB_URI)

router = APIRouter()

@router.get("/points")
def get_points():
    points = 5000
    return {'points': points}

@router.get("/statistics", response_model=List[BinsData])
def get_statistics():
    # Get card_id ID form log user ID -> TODO
    cartd_id = "43913389255"
    user_statistic = get_documents_by_card_id(cartd_id)
    return user_statistic

def get_documents_by_card_id(card_id):
    db = client['smartbin']
    open_bins = db.opened_bins
    card_id_documents = open_bins.find({'card_id': card_id})
    print(card_id_documents)
    final_data = []
    for document in card_id_documents:
        final_data.append(document)
    return final_data
    