#!/usr/bin/env python

__all__ = ['DBLogHandler']

import logging
from .log_handler import DBLogHandler

logging.getLogger(__file__).addHandler(DBLogHandler().setLevel(logging.ERROR))

'''
PS: Appologies for the apauling naming convensions used in this module.
'''
