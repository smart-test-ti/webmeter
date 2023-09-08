from core.sqlhandle import models, schemas, database
from typing import Optional
from loguru import logger

def create_task(tasks: schemas.taskCreate):
    with database.dbConnect() as session:
        result = session.query(models.Key).filter(models.Task.task == tasks.task).first()
        if(result is None):
            db_task = models.Task(plan=tasks.plan,task=tasks.task,model=tasks.model)
            session.add(db_task)
            session.commit()
            session.refresh(db_task)
        else:
            raise Exception('task is existed')    

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