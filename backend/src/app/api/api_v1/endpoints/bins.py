from fastapi import APIRouter, UploadFile, File       

from app import schemas
from app.crud import crud_bins

router = APIRouter()

@router.post("/bin_opened", status_code=201)
def bin_opened(bins: schemas.bin.BinsOpened):
    status = crud_bins.register_open_bin(bins=bins)
    return status


@router.post("/update_bin_status", status_code=201)
def update_bin_status(bins: schemas.bin.BinsStatus):
    status = crud_bins.update_bin_status(bins=bins)
    return status


@router.post("/upload_image/{transaction_id}", status_code=201)
def upload_image(transaction_id, file: bytes = File(...)):
    status = crud_bins.detect_recycle_status(transaction_id, file)
    return status


