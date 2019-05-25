#!/usr/bin/env python

'''
@author: puneet.reddy@beyondanalysis.net
@created: 20180515
@blurb: A custom log handler using sqlalchemy to send all log messages to 
    postgresql database.
'''

from datetime import datetime
from sqlalchemy import (Column, Sequence)
from sqlalchemy.types import (DateTime, Integer, String)
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    logger = Column(String)
    level = Column(String)
    source = Column(String)
    trace = Column(String)
    msg = Column(String)
    logged_at = Column(DateTime, default=func.now())

    def __init__(self, logger=None, source=None, level=None, trace=None, msg=None):
        self.logger = logger
        self.level = level
        self.source = source
        self.trace = trace
        self.msg = msg
        self.logged_at = datetime.utcnow()

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        #[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s
        log_time = self.logged_at.strftime('%m/%d/%Y-%H:%M:%S')
        return "<Log: %s - %s - %s - %s - %s - %s>" % (
            log_time, self.logger, self.level, self.source, self.trace, self.msg[:50])


