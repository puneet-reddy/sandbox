#!/usr/bin/env python

'''
@author: puneet.reddy@beyondanalysis.net
@craeted: 20180511
@blurb: This creates the model for the logs table in postgresql after
    checking that it does not exist.
'''

import os
import sqlalchemy
import sys
from sqlalchemy import (Table, Column)
from sqlalchemy.types import (Integer, String, DateTime)
from sqlalchemy.sql import func

from CustomLogging import config
from CustomLogging.log import Log



def table_ddl(db_name = None):
    config.POSTGRES['db'] = db_name or config.POSTGRES['db']
    db_url = "postgresql+psycopg2://{user}:{pass}@{host}:{port}/{db}".format(
        **config.POSTGRES)
    engine = sqlalchemy.create_engine(db_url)
    if not engine.dialect.has_table(engine, 'logs'):
        metadata = sqlalchemy.MetaData()
        metadata.bind = engine
        Table('logs', metadata,
              Column('id', Integer, primary_key=True),
              Column('logger', String),
              Column('level', String),
              Column('source', String),
              Column('trace', String),
              Column('msg', String),
              Column('logged_at', DateTime, default=func.now())
              )
        metadata.create_all()
        msg = 'Created table "logs".'
        return msg
    else:
        msg = 'Table "logs" already exists'
        return msg

if __name__ == '__main__':
    if len(sys.argv) == 2:
        table_ddl(sys.argv[1])
    else:
        table_ddl()
