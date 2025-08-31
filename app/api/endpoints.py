from fastapi import APIRouter
from fastapi import APIRouter, UploadFile, File
from ..services.process_pdf import process_pdf

route = APIRouter()

@route.get("/", response_model=dict)
async def health_check():
    return {"status": "healthy"}

@route.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    result = await process_pdf(file)
    return {"filename": file.filename, "message": result}

