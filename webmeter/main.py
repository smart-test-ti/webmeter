import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from public.utils import utils
import os

app = FastAPI(debug=True)
STATICPATH = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory=os.path.join(STATICPATH, 'templates'))


@app.get("/plan", response_class=HTMLResponse)
async def index(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})
if __name__ == "__main__":
   uvicorn.run("main:app", host=utils.local_ip(), port=6006, reload=False)
