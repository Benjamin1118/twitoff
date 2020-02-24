''' Minimal flask app'''

from flask import Flask

#make the app
app = Flask(__name__)

#make the route
@app.route('/')

#Now define the function
def: hello:
    return 'Hello World'

    