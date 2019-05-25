#!/usr/bin/env python3

import os

POSTGRES = {
    'user': os.getenv('POSTGRES_USER', 'postgres'),
    'pass': os.getenv('POSTGRES_PASS', 'postgres'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': os.getenv('POSTGRE_PORT', '5432'),
    'db': os.getenv('HUMANITI_DB', 'humaniti')
}
