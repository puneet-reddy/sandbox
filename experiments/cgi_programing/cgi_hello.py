#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi

print('Content-type:text/html\n\n')
print('<html><body>')
print('<h1>It works!</h1>')
form = cgi.FieldStorage()
if form.getvalue('name'):
    name = form.getvalue('name')
    print("<h1>Hello ", name, "! You're using CGI!</h1><br />")
if form.getvalue('happy'):
    print('<p>Yay! You are happy today!</p>')
if form.getvalue('sad'):
    print('<p>So sad that you are sad. </p>')

print("<form method='post' action='hello.py'>")
print("<p>Name: <input type='text' name='name'/></p>")
print("<input type='checkbox' name='happy'/>Happy")
print("<input type='checkbox' name='sad'/>Sad")
print("<input type='submit' value='Submit'/>")
print('</body></html>')