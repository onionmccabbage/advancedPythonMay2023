# we may need to pip install flask
from flask import Flask # NB capital 'F'
import requests

# flask is a proper web server. Handles basic HTML requests including parameters
app = Flask(__name__) # any name will do, by convention we use __name__

# next we declare routes (http pathways to content)
@app.route('/') # this is the ROOT of our service
def root():
    '''here we decide what content will be served at the root of our service'''
    return 'Welcome to this Flask server'

@app.route('/home') # here is a route for /home
def home():
    '''return some basic HTML'''
    content = '<h2>Nearly Done</h2><p>Here is the home page</p>'
    return content

# we can pass parameters to our route, but we need a default in the function
@app.route('/greet')
@app.route('/greet/<name>') # allow a parameter which will be called 'name'
def greet(name='Timnit'):
    '''respond with a greeting'''
    content = f'<h2>Greetings {name}</h2>'
    return content

# sometimes it is useful to have several routes resulting in the SAME response content
@app.route('/aluminium')
@app.route('/aluminum')
@app.route('/alluminum')
@app.route('/allumminum')
def al():
    return 'It is spelt Aluminium'

# we can make our server a proxy
@app.route('/json') # careful: we might need CORS permissions
@app.route('/json/<cat>') # this will leave the default id=1
@app.route('/json/<cat>/<id>') # this overrides user and id
def j(cat='albums', id=1):
    response = requests.get(f'https://jsonplaceholder.typicode.com/{cat}/{id}')
    response_j = response.json()
    # we could do anything here, e.g. db, file, alterations etc.
    return response_j


if __name__ == '__main__':
    app.run() # start our server
