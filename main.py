from typing import Optional
from fastapi import FastAPI, Response, Request
# Router - from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/views", StaticFiles(directory="./views"))

# CORS
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Router
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/web")
def web():
    viewFile = open(file='/Users/doylekim/my/pyweb/index.html', mode="r", encoding="utf-8")
    html_content = viewFile.read()
    viewFile.close()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/preview")
def preview():
    viewFile = open(file='/Users/doylekim/my/pyweb/preview.html', mode='r', encoding='utf-8', )
    html_content = viewFile.read()
    viewFile.close()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/preview2")
def preview2():
    viewFile = open(file='./views/preview2.html', mode='r', encoding='utf-8', )
    html_content = viewFile.read()
    viewFile.close()
    return HTMLResponse(content=html_content, status_code=200)


