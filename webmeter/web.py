import uvicorn
from fastapi import FastAPI
from webmeter.view import page,api
from webmeter.public.utils import Utils
import requests
import webbrowser
import multiprocessing
import os

app = FastAPI(debug=False)
app.include_router(page.router)
app.include_router(api.router)

def status(host: str, port: int) -> bool:
    r = requests.get('http://{}:{}/plan'.format(host, port), timeout=2.0)
    flag = (True, False)[r.status_code == 200]
    return flag

def start(host: str, port: int) -> None:
    uvicorn.run("webmeter.web:app", host=host, port=port, reload=False)

def open(host: str, port: int)  -> None:
    flag = True
    while flag:
        flag = status(host, port)
    webbrowser.open('http://{}:{}/plan'.format(host, port), new=2)

def main(host=Utils.ip(), port=6006) -> None:
    pool = multiprocessing.Pool(processes=2)
    pool.apply_async(start, (host, port))
    pool.apply_async(open, (host, port))
    pool.close()
    pool.join()    

if __name__ == "__main__":
    main()