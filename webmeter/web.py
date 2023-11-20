import uvicorn
import os
from fastapi import FastAPI
import requests
import webbrowser
import multiprocessing
from fastapi.staticfiles import StaticFiles
from loguru import logger
from webmeter.view import page,api
from webmeter.core.utils import Common
from webmeter.core.engine import EngineServie

app = FastAPI(debug=False)
app.include_router(page.router)
app.include_router(api.router)
STATICPATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
app.mount("/static", StaticFiles(directory=STATICPATH), name="static")


def status(host: str, port: int) -> bool:
    r = requests.get('http://{}:{}/plan'.format(host, port), timeout=2.0)
    flag = (True, False)[r.status_code == 200]
    return flag

def start(host: str, port: int) -> None:
    uvicorn.run("webmeter.web:app", host=host, port=port, reload=False)

def open_url(host: str, port: int)  -> None:
    flag = True
    while flag:
        flag = status(host, port)
    webbrowser.open('http://{}:{}/plan'.format(host, port), new=2)

def main(host=Common.ip(), port=6006, jmeter_server='off') -> None:
    if jmeter_server == 'off':
        pool = multiprocessing.Pool(processes=2)
        pool.apply_async(start, (host, port))
        pool.apply_async(open_url, (host, port))
        pool.close()
        pool.join()
    elif jmeter_server == 'on':
        EngineServie.check_JavaEnvironment()
        EngineServie.check_JmeterEnvironment()
        Common.exec_cmd(f'{EngineServie.JMETER_SERVER_PATH.get(Common.pc_platform())} -Djava.rmi.server.hostname={host}')
    else:
        logger.error('The value of jmeter_server is invalid.')        