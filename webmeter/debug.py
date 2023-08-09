import uvicorn
from fastapi import FastAPI
from view import page,api
from public.utils import Utils
import requests
import webbrowser

app = FastAPI(debug=True)
app.include_router(page.router)
app.include_router(api.router)

def status(host: str, port: int) -> bool:
    r = requests.get('http://{}:{}/plan'.format(host, port), timeout=2.0)
    flag = (True, False)[r.status_code == 200]
    return flag

def start(host: str, port: int) -> None:
    uvicorn.run("debug:app", host=host, port=port, reload=False)

def open(host: str, port: int) -> None:
    flag = True
    while flag:
        flag = status(host, port)
    webbrowser.open('http://{}:{}/plan'.format(host, port), new=2)

def main(host=Utils.ip(), port=6006) -> None:
    start(host, port)   

if __name__ == "__main__":
    main()
