import uvicorn
from fastapi import FastAPI
from webmeter.view import page,api
from webmeter.public.utils import utils
import requests
import webbrowser
import multiprocessing

app = FastAPI(debug=False)
app.include_router(page.router)
app.include_router(api.router)


def status(host: str, port: int):
    r = requests.get('http://{}:{}/plan'.format(host, port), timeout=2.0)
    flag = (True, False)[r.status_code == 200]
    return flag

def start(host: str, port: int):
    uvicorn.run("__main__:app", host=host, port=port, reload=False)

def open(host: str, port: int):
    flag = True
    while flag:
        flag = status(host, port)
    webbrowser.open('http://{}:{}/plan'.format(host, port), new=2)

def main(host=utils.local_ip(), port=6006):
    pool = multiprocessing.Pool(processes=2)
    pool.apply_async(start, (host, port))
    pool.apply_async(open, (host, port))
    pool.close()
    pool.join()    

# if __name__ == "__main__":
#     main()
