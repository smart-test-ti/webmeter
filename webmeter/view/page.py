from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi import APIRouter
import os

router = APIRouter()

STATICPATH = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory=os.path.join(STATICPATH, '..', 'templates'))


@router.get("/")
async def redirect_typer():
    return RedirectResponse("/plan")

@router.get("/plan", response_class=HTMLResponse)
async def plan(request: Request):
   return templates.TemplateResponse("plan.html", {"request": request})

@router.get("/result", response_class=HTMLResponse)
async def result(request: Request):
   return templates.TemplateResponse("result.html", {"request": request})

@router.get("/analysis/{plan}/{task}", response_class=HTMLResponse)
async def result(request: Request, plan: str, task: str):
   return templates.TemplateResponse("analysis.html", {"request": request, "plan": plan, "task": task})