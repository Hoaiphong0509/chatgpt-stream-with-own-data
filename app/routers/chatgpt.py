from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from app.services.chatgpt import chat_default, chat, chat_stream

router = APIRouter(prefix="/api/chatgpt", tags=["chatgpt"])

@router.get('/')
def endpoint():
    return JSONResponse(status_code=200, content={'data': 'Hello world 💫'}) 


@router.post('/chat-default')
def chat_default_endpoint(data: dict):
    query = data.get('query')
    if query:
        result = chat_default(query)
        return JSONResponse(status_code=200, content={'answer': result}) 
    else:
        raise HTTPException(status_code=400, detail='Invalid request')


@router.post('/chat')
def chat_endpoint(data: dict):
    try:
        query = data.get('query')
        if query:
            result = chat(query)
            return JSONResponse(status_code=200, content={'answer': result}) 
        else:
            raise HTTPException(status_code=400, detail='Invalid request')
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=500, detail=error_message)
    
@router.post('/chat-stream')
def chat_endpoint(data: dict):
    try:
        query = data.get('query')
        if query:
            generator = chat_stream(query)
            return StreamingResponse(generator, media_type="text/event-stream")
        else:
            raise HTTPException(status_code=400, detail='Invalid request')
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=500, detail=error_message)