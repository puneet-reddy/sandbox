#!/usr/bin/env python

'''
@author: puneet.reddy@beyondanalysis.net
@created: 20180507
@blurb: Renders the flask API template using inputs from the
    RAML spec.
'''

from jinja2 import (Environment, PackageLoader, select_autoescape)

env = Environment(
    loader=PackageLoader('raml2flask', '.'), 
    autoescape=select_autoescape(['html', 'xml']))

def is_endpoint(odict_in):
    #To avoid mutation during iteration.
    odict_out = odict_in.copy()
    for key in odict_in.keys():
        if not key.startswith(r'/'):
            del odict_out[key]
    return odict_out

env.filters['is_endpoint'] = is_endpoint

ft = env.get_template('flask_app.jinja2')

def do(template, params):
    return template.render(raml=params)
