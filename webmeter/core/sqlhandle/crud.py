from core.sqlhandle import models, schemas, database
from typing import Optional

def create_task(task: schemas.taskCreate):
    with database.dbConnect() as session:
        db_task = models.Task(plan=task.plan,task=task.task,model=task.model)
        session.add(db_task)
        session.commit()
        session.refresh(db_task)

def create_key(key: schemas.keyCreate):
    with database.dbConnect() as session:
        db_key = models.Key(key=key.key, value=key.value)
        session.add(db_key)
        session.commit()
        session.refresh(db_key)


def query_key(key: schemas.keyQuery):
    with database.dbConnect() as session:
        value = session.query(models.Key).filter(models.Key.key == key.key).first()
        return value   