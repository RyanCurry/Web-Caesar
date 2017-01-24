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
import Caesar
import cgi

def build_page(content):
    encryptbox="<textarea name='message'>" + content + "</textarea>"
    button="<input Type='submit'/>"
    rotate="<input Type='number' name='rot'/>"
    message_label="<label>Type a message:</label>"
    rot_label="<label>Pick a number to rotate by:</label>"
    form="<form method='post'>" + rot_label + rotate + '<br>'  + message_label + '<br>'  + encryptbox + "<br>" + button + "</form>"
    header="<h2>Web Caesar</h2>"
    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(build_page(""))

    def post(self):
        mes= self.request.get("message")
        rotation= self.request.get("rot")
        encryptedmes=Caesar.encrypt(mes,rotation)

        escaped_message=cgi.escape(encryptedmes)

        self.response.write(build_page(escaped_message))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
