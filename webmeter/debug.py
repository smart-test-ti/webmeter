import uvicorn
from fastapi import FastAPI
from view import page,api
from public.utils import utils
import requests
import webbrowser

app = FastAPI(debug=True)
app.include_router(page.router)
app.include_router(api.router)

def status(host: str, port: int):
    r = requests.get('http://{}:{}/plan'.format(host, port), timeout=2.0)
    flag = (True, False)[r.status_code == 200]
    return flag

def start(host: str, port: int):
    uvicorn.run("web:app", host=host, port=port, reload=False)

def open(host: str, port: int):
    flag = True
    while flag:
        flag = status(host, port)
    webbrowser.open('http://{}:{}/plan'.format(host, port), new=2)

def main(host=utils.local_ip(), port=6006):
    start(host, port)   

if __name__ == "__main__":
    main()
