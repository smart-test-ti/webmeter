from sqlalchemy import Boolean, Column, Integer, String, DateTime, Float
from webmeter.core.sqlhandle.database import Base
import datetime


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    plan = Column(String, index=True)
    task = Column(String, index=True, unique=True)
    model = Column(String, index=True, default='stand-alone') #stand-alone | distributed
    success_num = Column(Integer, index=True, default=0)
    fail_num = Column(Integer, index=True, default=0)
    threads = Column(Integer, index=True, default=1)
    status = Column(String, index=True, default='Running')
    stime = Column(String, index=True)
    etime = Column(String, index=True)

class Monitor(Base):
    __tablename__ = "monitor"

    id = Column(Integer, primary_key=True, index=True)
    machine = Column(String, index=True, unique=True)
    task =  Column(String, index=True, unique=True)
    cpu = Column(Float, index=True, default=0)
    memory = Column(Float, index=True, default=0)
    network = Column(Float, index=True, default=0)
    ctime = Column(String, index=True, default=None)

class Key(Base):
    __tablename__ = "key"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True, unique=True)
    value = Column(String, index=True)
