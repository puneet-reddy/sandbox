#!/usr/bin/env python3

import logging
import os
import sqlalchemy
import sys
import unittest

from unittest import TestCase
from sqlalchemy_utils import database_exists

from CustomLogging import config
from CustomLogging.log_handler import DBLogHandler
from CustomLogging.init_db import table_ddl

class TestLogging(TestCase):
        
    def setUp(self):
        config.POSTGRES['db'] = 'testdb'
        url = "postgresql+psycopg2://{user}:{pass}@{host}:{port}/{db}".format(
            **config.POSTGRES)
        self.engine = sqlalchemy.create_engine(url)
        if not database_exists(self.engine.url):
            self.skipTest("Database 'testdb' is required and does not exist.")
        self.connection = self.engine.connect()
        table_ddl(config.POSTGRES['db'])

    def test_init_db(self):
        self.assertTrue(
            self.engine.dialect.has_table(self.engine, 'logs'), 
            "Table logs not created by init_db script")

    def test_logging(self):
        logger = logging.getLogger(__file__)
        handler = DBLogHandler(config.POSTGRES['db'])
        handler.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        logger.info('test')
        res = self.connection.execute(
            'select * from logs order by logged_at desc;').fetchone()
        self.assertIsNotNone(res, "No log was found in the db.")
        self.assertEqual('test', res[5], "Log message mismatch in db.")

    def tearDown(self):
        self.connection.execute('DROP TABLE logs;')

    def __del__(self):
        self.connection.close()

if __name__ == '__main__':
    sys.argv.insert(1, '--verbose')
    unittest.main(argv=sys.argv)
