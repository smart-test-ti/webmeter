from sqlalchemy import Boolean, Column, Integer, String, DateTime, Float
from core.sqlhandle.database import Base
import datetime


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    plan = Column(String, index=True)
    task = Column(String, index=True, unique=True)
    model = Column(String, index=True)
    status = Column(String, index=True, default='runing')
    success_num = Column(Integer, index=True, default=0)
    fail_num = Column(Integer, index=True, default=0)
    ctime = Column(DateTime, default=datetime.datetime.now)
    is_active = Column(Boolean, default=True)

class Monitor(Base):
    __tablename__ = "monitor"

    id = Column(Integer, primary_key=True, index=True)
    machine = Column(String, index=True, unique=True)
    task =  Column(String, index=True, unique=True)
    cpu = Column(Float, index=True, default=0)
    memory = Column(Float, index=True, default=0)
    network = Column(Float, index=True, default=0)
    ctime = Column(DateTime, index=True, default=None)

class Key(Base):
    __tablename__ = "key"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True, unique=True)
    value = Column(String, index=True)
