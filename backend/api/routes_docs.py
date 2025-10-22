from fastapi import APIRouter, UploadFile
import os
from core.utils import extract_text_from_pdf
from core.embeddings import create_embeddings

router = APIRouter(prefix="/docs", tags=["Documents"])

UPLOAD_DIR = "backend/data/user_uploads"

@router.post("/upload")
async def upload_document(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    create_embeddings(text, file.filename)
    return {"message": f"File {file.filename} uploaded and embedded!"}
