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
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

'''


from google.appengine.ext import webapp 
from google.appengine.ext.webapp.util import run_wsgi_app

class IndexHandler(webapp.RequestHandler): 
    def get(self): 
        if self.request.url.endswith('/'): 
            path = '%sindex.html'%self.request.url

        self.redirect(path)

    def post(self): 
        self.get()

application = webapp.WSGIApplication([('/.*', IndexHandler)], debug=True)

def main(): 
    run_wsgi_app(application)

if __name__ == "__main__": 
    main()
