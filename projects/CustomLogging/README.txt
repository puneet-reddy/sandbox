A very basic logger to handling logging to postgresql db


Expects the following env variables:

POSTGRES_USER
POSTGRES_PASS
POSTGRES_HOST
POSTGRES_PORT
HUMANITI_DB


Example Usage:

import logging

# Logger setup
logger = logging.getLogger(__file__)
logger.setLevel(logging.WARN)
handler = DBLogHandler('testdb')
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

#This gets logged to the testdb.logs
logger.error('Something bad happened!') 

Installation:
Simply -
python setup.py install