#!/usr/bin/env python

'''
This first part is just a very simple WSGI app using falcon
'''

import falcon

class ThingsResource(object):
    def on_get(self, req, res):
        '''Handles the GET requests'''
        res.status = falcon.HTTP_200
        res.body = ('\nTwo things awe me most, the starry sky '
                    'avove me and the moral law within me. \n'
                    '\n'
                    ' ~ Immanuel Kant\n\n')
        

app = falcon.API()
things = ThingsResource()
app.add_route('/', things)

'''
Here we use bjoern to host the WSGI app
'''

import bjoern
if __name__ == '__main__':
    bjoern.run(app, 'localhost', 8080)
