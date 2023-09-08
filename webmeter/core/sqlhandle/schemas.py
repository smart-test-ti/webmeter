from typing import Optional
from pydantic import BaseModel


class TaskBase(BaseModel):
    status: Optional[str] = None
    model: Optional[str] = None
    is_active: bool
    success_num: int
    fail_num: int

class taskCreate(TaskBase):
    plan: str
    task: str

class taskQuery(TaskBase):
    id: int
    plan: str
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
    machine: str
    task: str

class monitorQuery(monitorBase):
    id: int
    task: str
    class Config:
        from_attributes = True

