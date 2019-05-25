
#!/usr/bin/env python

import io
import os
import pip
import re
import sys


def up_n(n, path):
    while n > 0:
        path = os.path.dirname(path)
        n -= 1
    return path


hum_dir = up_n(2, os.path.abspath(__file__))


def find_apps(hum_dir):
    app_files = []
    for root, _, files in os.walk(hum_dir):
        if root.find('__pycache__') <= 0:
            for file_ in files:
                with io.open(os.path.join(root, file_)) as obj:
                    try:
                        if re.search(r'Flask\(__name__\)', obj.read()):
                            app_files.append(os.path.join(root, file_))
                    except UnicodeDecodeError:
                        pass  # We don't care about files we can't understand
        else:
            print("Skipping: {}".format(root))
    return app_files


# Template for the wsgi file
template = '''
import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, r'{}')

from {} import app as application
'''


def build_wsgi(file_list):
    wsgi_files = []
    for file_ in file_list:
        file_path, file_name = os.path.split(file_)
        # Backtrack and build the path to the module root
        module_path = ''
        path_sentinel = file_path
        while os.path.exists(os.path.join(path_sentinel, '__init__.py')):
            module_path = os.path.split(path_sentinel)[1] + '.' + module_path
            path_sentinel = os.path.split(path_sentinel)[0]

        wsgi_code = template.format(path_sentinel, module_path.rstrip('.'))

        wsgi_path = os.path.join(
            path_sentinel, os.path.splitext(file_name)[0]+'.wsgi')
        with open(wsgi_path, 'w+') as wsgi_file:
            wsgi_file.write(wsgi_code)
        wsgi_files.append(wsgi_path)
    return wsgi_files


def find_requirements(hum_dir):
    req_files = []
    for root, _, files in os.walk(hum_dir):
        if root.find('__pycache__') <= 0:
            for file_ in files:
                if os.path.split(file_)[1] == 'requirements.txt':
                    req_files.append(os.path.join(root, file_))
        else:
            print("Skipping: {}".format(root))
    return req_files


def install_requirements(req_list):
    for req in req_list:
        print("Installing requirements from: {}".format(req))
        pip.main(['install', '-r' '{}'.format(req)])


def build_a2_config(wsgi_files):
    config_start = r'''
    <VirtualHost *:80>
        WSGIPassAuthorization On
    '''
    config_end = r'''
    </VirtualHost>
    '''
    config_template = r'''
        WSGIScriptAlias /{} {}
        <Directory {}>
            Require all granted
        </Directory>
    '''
    config_code = ''
    for each in wsgi_files:
        placeholder_path = os.path.dirname(each)
        while os.path.split(placeholder_path)[1] != 'api':
            placeholder_path = os.path.split(placeholder_path)[0]
        component = os.path.split(placeholder_path)[1]
        config_code += config_template.format(
            component,
            each,
            os.path.join(placeholder_path, 'api')
        )

    config_code = config_start + config_code + config_end
    if os.path.exists('/etc/apache2/sites-enabled'):
        conf_path = "/etc/apache2/sites-enabled/api_server.conf"
    else:
        conf_path = 'api_server.conf'

    with open(conf_path, 'w+') as api_config:
        api_config.write(config_code)

    print("Generated server configuration at: {}".format(
        os.path.abspath(conf_path)))


if __name__ == '__main__':
    from pprint import pprint as pp
    if not len(sys.argv) == 2:
        print("Usage: python {} <path to deployment git repo>".format(__file__))
        sys.exit(-1)

    base_path = sys.argv[1]
    app_files = find_apps(base_path)
    pp(app_files)
    wsgi_files = build_wsgi(app_files)
    req_files = find_requirements(base_path)
    pp(req_files)
    install_requirements(req_files)
    build_a2_config(wsgi_files)
