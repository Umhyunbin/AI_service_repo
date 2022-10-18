import uvicorn

from fastapi import FastAPI, Request
from api.serving import serving

app = FastAPI()

app.include_router(serving, prefix='/api/v1', tags=['serving'])

if __name__ == '__main__':
    # uvicorn app: app --reload --host = 0.0.0.0 --port = 8080
    uvicorn.run(app, host='0.0.0.0', port=8080)

