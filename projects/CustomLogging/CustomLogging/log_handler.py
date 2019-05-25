#!/usr/bin/env python

'''
@author: puneet.reddy@beyondanalysis.net
@created: 20180515
@blurb: A custom log handler using sqlalchemy to send all log messages to 
    postgresql database.
    Each instance of the logger creates and holds a connection to the DB.
'''


import logging
import traceback

from sqlalchemy import (create_engine, MetaData)
from sqlalchemy.orm import sessionmaker

from  CustomLogging import config
from CustomLogging.log import Log

class DBLogHandler(logging.Handler):
    '''
    A very basic logger to handling logging to postgresql db
    '''

    def __init__(self, db=None):
        config.POSTGRES['db'] = db or config.POSTGRES['db']
        db_uri = "postgresql+psycopg2://{user}:{pass}@{host}:{port}/{db}".format(
            **config.POSTGRES)
        self.engine = create_engine(db_uri)
        self.meta = MetaData(self.engine)
        self.session = sessionmaker(self.engine)()
        super(DBLogHandler, self).__init__(logging.DEBUG)

    def emit(self, record):
        '''
        Format and send the log to postgres db.
        Table format is:
        name, levelname, pathname:lineno, message, logged_at
        '''
        try:
            trace = None
            exc = record.__dict__['exc_info']
            if exc:
                trace = traceback.format_exc()
            log = Log(
                logger=record.__dict__['name'],
                level=record.__dict__['levelname'],
                source=record.__dict__['pathname'] +
                ':'+str(record.__dict__['lineno']),
                trace=trace,
                msg=record.__dict__['msg']
            )
            self.session.add(log)
            self.session.commit()
        except Exception as exc:
            print("CRITICAL error in logging! {}".format(str(exc)))
            raise exc
