from typing import Optional
from pydantic import BaseModel
import datetime



class TaskBase(BaseModel):
    model: Optional[str] = None
    threads: int
    success_num: int
    fail_num: int
    status: str
    etime: datetime.datetime

class taskCreate(BaseModel):
    plan: str
    task: str
    model: str

class taskQuery(BaseModel):
    plan: str
    class Config:
        from_attributes = True

class taskDetail(TaskBase):
    plan: str
    task: str
    class Config:
        from_attributes = True

class taskUpdate(TaskBase):
    plan: str
    task: str
    class Config:
        from_attributes = True

class KeyBase(BaseModel):
    key: Optional[str] = None

class keyCreate(KeyBase):
    key: str
    value: Optional[str] = None

class keyUpdate(KeyBase):
    key: str
    value: Optional[str] = None

class keyQuery(KeyBase):
    key: str
    class Config:
        from_attributes = True

class monitorBase(BaseModel):
    cpu: float
    memory: float
    network: float

class monitorCreate(monitorBase):
    machine: float
    task: float

class monitorQuery(monitorBase):
    id: int
    task: str
    class Config:
        from_attributes = True

