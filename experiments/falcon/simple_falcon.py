#!/usr/bin/env python3

import falcon
import bjoern

class DemoResource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = ('\nTwo things awe me most, the starry sky '
                    'above me and the moral law within me.\n'
                    '\n'
                    '    ~ Immanuel Kant\n\n')

app = falcon.API()
demo = DemoResource()
app.add_route('/', demo)

if __name__ == '__main__':
    host, port = 'localhost', 5000
    print(f'Starting app on {host}:{port}')
    bjoern.run(app, host, port)
