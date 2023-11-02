import re
import os

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse


from app.services.vector import allowed_file, create_vector, secure_filename

router = APIRouter(prefix="/api/vector", tags=["vector"])

@router.get('/')
def endpoint():
    return JSONResponse(200, {'data': 'Hello world 💫'}) 


@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    if not file:
        return JSONResponse(status_code=400, content={'error': 'No file part'})

    if file.filename == '':
        return JSONResponse(status_code=400, content={'error': 'No selected file'})

    if not allowed_file(file.filename):
        return JSONResponse(status_code=400, content={'error': 'File type not allowed. Accept only: pdf, txt'})

    filename = secure_filename(file.filename)
    filename = re.sub(r'[^\w.-]', '_', filename)
    filename = re.sub(r'__+', '_', filename)
    filename = filename.strip()
    filename = filename.lower()

    file_path = os.path.join('app/assets', filename)
    with open(file_path, 'wb') as f:
        f.write(await file.read())

    return JSONResponse(status_code=200, content={'message': 'File uploaded successfully'})

@router.post('/generate')
def generate_vector():
    try:
        create_vector()
        return JSONResponse(status_code=200, content={'message': 'Generate successfully'})
    except Exception as e:
        error_message = str(e)
        return HTTPException(status_code=500, detail=error_message)