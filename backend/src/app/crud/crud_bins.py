import os
import sys
import uuid
from io import BytesIO

import matplotlib.pyplot as plt
import pymongo
import requests
from app.schemas import bin
from app.crud.image_recognition import recognize_image


MONGODB_URI = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(MONGODB_URI)


def register_open_bin(bins: bin.BinsOpened):
    transaction_id = insert_document_mongo_db(bins, collection='opened_bins')
    return {"transaction_id": transaction_id}

def update_bin_status(bins: bin.BinsStatus):
    insert_or_update_bin_status(bins, collection='bins_status')
    return {"Status: OK"}

def detect_recycle_status(transaction_id, image):
    print(transaction_id)
    trash_type = recognize_image(image)
    update_recycle_status(collection='opened_bins', transaction_id=transaction_id, trash_type=trash_type)
    return {"Status: OK"}


# ------- HELPER FUNCTIONS ---------- #

def insert_document_mongo_db(data, collection):
    db = client['smartbin']
    open_bins = db[collection]
    post_data = dict(data)
    transaction_id = str(uuid.uuid4())
    post_data['transaction_id'] = transaction_id
    result = open_bins.insert_one(post_data)
    return transaction_id

def insert_or_update_bin_status(data, collection):
    db = client['smartbin']
    bins_status = db[collection]
    data = dict(data)
    bin_ =  bins_status.find_one({'bin_id': data['bin_id']})
    if not bin_:
        # insert data to mongo
        insert_document_mongo_db(data, collection='bins_status')
    else:
        # update data in mongodb
        myquery = { "bin_id": data['bin_id'] }
        newvalues = { "$set": { "waste_status": data["waste_status"], "timestamp": data["timestamp"] } }
        result = bins_status.update_one(myquery, newvalues)


def update_recycle_status(collection, transaction_id, trash_type):
    db = client['smartbin']
    bins_status = db[collection]
    bin_type = bins_status.find_one({"transaction_id": transaction_id})["bin_type"]
    print(bin_type, trash_type)
    if trash_type == bin_type:
        mongodb_update_value(bins_status, {"transaction_id": transaction_id}, {"recycle_status_ok": True})


def mongodb_update_value(collection, query, new_value):
    myquery = query
    newvalues = {"$set": new_value}
    result = collection.update_one(myquery, newvalues)



# def get_documents_by_card_id(client, card_id):
#     db = client['smartbin']
#     open_bins = db.opened_bins
#     card_id_documents = open_bins.find({'card_id': card_id})
#     for document in card_id_documents:
#         print(document)


