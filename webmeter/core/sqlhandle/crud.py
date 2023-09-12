from core.sqlhandle import models, schemas, database
from typing import Optional
from loguru import logger
import os, shutil, datetime
from core.plan import TestPlan

def create_task(tasks: dict):
    with database.dbConnect() as session:
        cur_time = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        result = session.query(models.Task).filter(models.Task.task == tasks['task']).first()
        if(result is None):
            db_task = models.Task(plan=tasks['plan'],task=tasks['task'],
                                  model=tasks['model'], threads=tasks['threads'],
                                  stime=cur_time, etime=cur_time)
            session.add(db_task)
            session.commit()
            session.refresh(db_task)
        else:
            raise Exception('{} is existed'.format(result.task))    

def update_task(tasks: dict):
    with database.dbConnect() as session:
        cur_time = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        result = session.query(models.Task).filter(models.Task.task == tasks['task']).first()
        if(result):
            result.success_num = tasks.get('success_num')
            result.fail_num = tasks.get('fail_num')
            result.status = tasks.get('status')
            result.etime = cur_time
            session.commit()
            session.refresh(result)
        else:
            raise Exception('{} is not existed'.format(result.task))
        
def query_task_one(tasks: schemas.taskQuery):
    with database.dbConnect() as session:
        results = session.query(models.Task).filter(models.Task.plan == tasks.plan).all()
        result_dict = [result.task for result in results]
        return result_dict

def query_task_all():
    with database.dbConnect() as session:
        results = session.query(models.Task).order_by(models.Task.stime.desc()).all()
        result_dict = [{'plan': result.plan, 'task':result.task,
                        'model': result.model, 'status': result.status,
                        'threads': result.threads, 'success_num': result.success_num,
                        'fail_num': result.fail_num, 'stime': result.stime,
                        'etime': result.etime}  for  result in results]
        return result_dict

def remove_task_one(plan: str, task: str):
    logger.warning('remove task data : {}'.format(task))
    TASK_LOG_DIR = os.path.join(os.getcwd(), 'webmeter', plan, 'log', task)
    TASK_REPORT_DIR = os.path.join(os.getcwd(), 'webmeter', plan, 'report', task)
    with database.dbConnect() as session:
        session.query(models.Task).filter(models.Task.plan == plan,
                                           models.Task.task == task).delete()

    if os.path.exists(TASK_LOG_DIR):
        shutil.rmtree(TASK_LOG_DIR, True)

    if os.path.exists(TASK_REPORT_DIR):
        shutil.rmtree(TASK_REPORT_DIR, True)
        
def remove_task_all():
    logger.warning('remove all task datas')
    with database.dbConnect() as session:
        session.query(models.Task).delete()
    plan = TestPlan()
    for item in plan.get_all_plan():
        shutil.rmtree(os.path.join(plan.root_dir, item.get('name'), 'log'), True)
        shutil.rmtree(os.path.join(plan.root_dir, item.get('name'), 'report'), True)    

def create_key(keys: schemas.keyCreate):
    with database.dbConnect() as session:
        result = session.query(models.Key).filter(models.Key.key == keys.key).first()
        if(result is None):
            db_key = models.Key(key=keys.key, value=keys.value)
            session.add(db_key)
            session.commit()
            session.refresh(db_key)

def update_value(keys: schemas.keyUpdate):
    with database.dbConnect() as session:
        result = session.query(models.Key).filter(models.Key.key == keys.key).first()
        if(result.key):
            result.value = keys.value
            session.commit()
        else:
            raise Exception('key not existed')

def query_key(keys: schemas.keyQuery):
    with database.dbConnect() as session:
        result = session.query(models.Key).filter(models.Key.key == keys.key).first()
        return result.value   