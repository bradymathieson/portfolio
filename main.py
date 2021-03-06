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
Portfolio

Created a portfolio, deployed at:

    http://bradymath.co (!!!) or
    http://brady-portfolio-206.appspot.com 

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

        if path == '/index.html':
            page_title = 'Home'

        elif path == '/resume.html':
            page_title = 'Resume'

        elif path == '/about.html':
            page_title = 'About'

        elif path == '/photo.html':
            page_title = 'Photos'

        elif path == '/projects.html':
            page_title = 'Projects'

        elif path == '/contact_success.html':
            page_title = 'Thank You!'


        template = JINJA_ENVIRONMENT.get_template('templates' + path)
        self.response.write(template.render({'title': page_title}))


class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'title': 'Contact'}))


app = webapp2.WSGIApplication([
    ('/', PageHandler),
    ('/index.html', PageHandler),
    ('/about.html', PageHandler),
    ('/photo.html', PageHandler),
    ('/resume.html', PageHandler),
    ('/contact.html', ContactHandler),
    ('/contact_success.html', PageHandler),
    ('/projects.html', PageHandler)
], debug=True)
