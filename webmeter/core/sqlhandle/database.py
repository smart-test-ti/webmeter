from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from loguru import logger
import os
from webmeter.core.utils import Common

SQL_DIR = Common.make_dir(os.path.join(os.getcwd(), 'webmeter'))
SQLALCHEMY_DATABASE_URL = "sqlite:///{}/webmeter_app.db".format(SQL_DIR)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@contextmanager
def dbConnect():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(e)
    finally:
        session.close()