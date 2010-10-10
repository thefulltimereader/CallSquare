import cgi

from os import path
from google.appengine.api import users
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.template import render
from google.appengine.ext.webapp.util import run_wsgi_app


class Greeting(db.Model):
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')
        greetings = Greeting.all().order('-date').fetch(10)
        context = {
            'greetings': greetings
        ,}
        tmpl = path.join(path.dirname(__file__), 'response.html')
        self.response.out.write(render(tmpl, context))
        
class GuestBook(webapp.RequestHandler):
    def post(self):
        greeting = Greeting()
        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/')

application = webapp.WSGIApplication([
    ('/', MainHandler),
    ('/sign', GuestBook),
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()