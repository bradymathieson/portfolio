#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import os
import logging
import jinja2

"""
main.py
BRADY MATHIESON - bradmath
SI 206 - Agile Web Development
Template Homework (Homework 3)

Created a four page portfolio with a login page, deployed at:

    http://template-homework-brady-si206.appspot.com

"""

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class PageHandler(webapp2.RequestHandler):
    def get(self):
        path = self.request.path
        if len(path) == 1:
            path = '/index.html'

        elif path == '/index.html':
            page_title = 'HOME'

        elif path == '/about.html':
            page_title = 'ABOUT'

        elif path == '/photo.html':
            page_title = 'PHOTOS'

        elif path == '/photo.html':
            page_title = 'PHOTOS'

        elif path == '/friends.html':
            page_title = 'FRIENDS'

        template = JINJA_ENVIRONMENT.get_template('templates' + path)
        self.response.write(template.render({'title': page_title}))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'title': 'LOGIN', 'header': 'Login'}))

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        if (self.request.get('username') == 'Colleen' and self.request.get('password') == 'pass'):
            template = JINJA_ENVIRONMENT.get_template('templates/login2.html')
            self.response.write(template.render({'title': 'SUCCESS', 'header': 'Logged in...'}))
        else:
            logging.info("Incorrect username: " + username)
            logging.info("Incorrect password: " + password)
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'title': 'LOGIN', 'header': 'Login', 'msg': 'Bad credentials. Try again.'}))


app = webapp2.WSGIApplication([
    ('/', PageHandler),
    ('/index.html', PageHandler),
    ('/about.html', PageHandler),
    ('/photo.html', PageHandler),
    ('/resume.html', PageHandler),
    ('/login.html', LoginHandler),
    ('/login2.html', LoginHandler)
], debug=True)
