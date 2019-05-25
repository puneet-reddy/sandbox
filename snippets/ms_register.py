#!/usr/bin/env python

'''
@author: puneet.reddy@beyondanalysis.net
@created:
@blurb: Simple script to register users on the MoneySoft system.
'''


import requests
import json
import logging

from auth_handler import Token
from CustomLogging import DBLogHandler

logger = logging.getLogger(__name__)
handler = DBLogHandler()
logger.addHandler(handler)
handler.setLevel(logging.WARN)
logger.setLevel(logging.WARN)

def ms_register(email, password, first_name, last_name):
    base_url = 'https://sandbox.moneysoft.com.au/api'
    ac_register_url = base_url + '/2.0/Account/Register'
    user_register_url = base_url + '/2.0/User/Register'

    ac_payload = json.dumps({
        'Email': email,
        'Firstname': first_name,
        'Lastname': last_name,
        'Password': password,
        'ConfirmPassword': password,
        'AgreesToTerms': True
    })

    usr_payload = json.dumps({
        'Username': email,
        'Password': password
    })

    h_token = Token()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(h_token.access_token)
    }

    try:
        res_1 = requests.post(ac_register_url, json=ac_payload, headers=headers)
        res_2 = requests.post(user_register_url, json=usr_payload, headers=headers)
        if res_1.ok:
            ms_id = res_1.json().get('Id')
        else:
            return None
    except Exception as err:
        logger.error(str(err))
        return None


