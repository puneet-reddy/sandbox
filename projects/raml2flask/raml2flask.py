#!/usr/bin/env python

'''
@author: puneet.reddy@beyondalaysis.net
@created: 20180502
@blurb: Takes an RAML document and tries to generate a working flask-restful
    based API stub
'''

# TODO: Remove this once everything is properly packaged.
import sys
sys.path.append(r'C:\Users\css112720\Desktop\beyond_analysis\humaniti\code')

import io
import logging
import os
import errno
import ramlfications
from jinja2 import (Environment, PackageLoader, select_autoescape)
from pprint import pprint as pp
try:
    from CustomLogging import DBLogHandler as Handler
except:
    from logging.handlers import StreamHandler as Handler


class Raml2Flask():
    '''
    Creates a flask-restful based skeleton from a valid 0.8 RAML specification.
    '''

    def __init__(self, raml_uri):
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        print(self.base_path)
        api_name = os.path.splitext(os.path.split(raml_uri)[1])[0] + '_api'
        api_dir = os.path.join(self.base_path, api_name)
        if not os.path.exists(api_dir):
            try: # In the event the directory is created right after we checked
                os.makedirs(api_dir)
            except OSError as err:
                if err.errno != errno.EEXIST:
                    raise
        self.ddl_out = os.path.join(api_dir, 'ddl.py')
        self.schema_out = os.path.join(api_dir, 'schema.py')
        self.api_out = os.path.join(api_dir, 'skeleton.py')
        self.api_file = raml_uri
        self.raml = self._load_raml()
        logger = logging.getLogger(__name__)
        handler = Handler()
        handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        self.logger = logger
        self.env = self._setup_env()

    def _setup_env(self, package='raml2flask', template_folder=None):
        if not template_folder:
            template_folder = os.path.join(self.base_path, 'templates')
        '''Setup for the jinja environment'''
        env = Environment(loader=PackageLoader(package, template_folder), )

        def find(key, dictionary):
            for k, v in dictionary.items():
                if k == key:
                    yield v
                elif isinstance(v, dict):
                    for result in find(key, v):
                        yield result
                elif isinstance(v, list):
                    for d in v:
                        for result in find(key, d):
                            yield result

        def find_example(dictionary):
            ex = find('example', dictionary)
            try:
                return ex.__next__()
            except:
                return "No example found."

        env.filters['find_example'] = find_example

        return env

    def _load_raml(self):
        raml = {}
        try:
            raml = ramlfications.load(self.api_file)
        except Exception as exc:
            self.logger.error(str(exc))
        return raml

    def generate_ddl(self, raml):
        try:
            schemas = {list(e.keys())[0]: list(e.values())[0]
                       for e in raml.get('schemas')}
            db_template = self.env.get_template('db_schema.jinja2')
            rendered = db_template.render(schemas=schemas)
            with io.open(self.ddl_out, 'w') as ddl_out:
                ddl_out.write(rendered)
            return True
        except Exception as exc:
            self.logger.error(str(exc), exc_info=True)
            return False

    def generate_schemas(self, raml):
        try:
            schemas = {list(e.keys())[0]: list(e.values())[0]
                       for e in raml.get('schemas')}
            schema_template = self.env.get_template('marsh_schema.jinja2')
            rendered = schema_template.render(schemas=schemas)
            with io.open(self.schema_out, 'w') as schema_out:
                schema_out.write(rendered)
            return True
        except Exception as exc:
            self.logger.error(str(exc), exc_info=True)
            return False

    def generate_api(self, raml):
        try:
            app_template = self.env.get_template('flask_app.jinja2')
            endpoints = {e: raml.get(e)
                         for e in raml.keys() if e.startswith(r'/')}
            flask_app = app_template.render(endpoints=endpoints)
            with io.open(self.api_out, 'w') as api_out:
                api_out.write(flask_app)
            return True
        except Exception as exc:
            self.logger.error(str(exc), exc_info=True)
            return False

    def generate_all(self):
        self.generate_ddl(self.raml)
        print("ORM DDL generated.")
        self.generate_schemas(self.raml)
        print("Marshamllow schemas generated.")
        self.generate_api(self.raml)
        print("API stubs generated.")
        return True

    def run_test_server(self):
        if os.path.isfile(self.api_out):
            print("Starting test server...")
            os.system(f'python {self.api_out}')
        else:
            print(f"Generated API not found at {self.api_out}")


if __name__ == '__main__':
    api_file = r'C:\Users\css112720\humaniti\signup.raml'
    flask_gen = Raml2Flask(api_file)
    flask_gen.generate_all()
    try:
        flask_gen.run_test_server()
    except KeyboardInterrupt:
        print("Server stopped.")
        
