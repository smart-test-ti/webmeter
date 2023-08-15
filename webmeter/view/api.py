from fastapi import APIRouter
from public.plan import TestPlan
import logging

router = APIRouter()
test_plan = TestPlan()

@router.post("/api/language")
async def language(content: dict):
   response = {'status':1}
   return response


@router.post("/api/plan/all")
async def get_all_plan():
   try:
      plan_list = test_plan.get_all_plan()
      result = {'status':1, 'plan_list':plan_list, 'length':len(plan_list), 'msg': 'get success'}
   except Exception as e:
      logging.exception(e)
      result = {'status':0, 'msg': str(e)}
   return result


@router.post("/api/plan/create")
async def create_plan(content: dict):
   plan_name = content.get('plan_name')
   try:
      if not test_plan.isexist(plan_name):
         test_plan.create(plan_name)
         result = {'status':1, 'msg': 'create success'}
      else:
         result = {'status':0, 'msg': 'plan existed'}   
   except Exception as e:
      logging.exception(e)
      result = {'status':0, 'msg': str(e)}
   return result