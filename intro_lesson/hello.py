''' Minimal flask app'''

from flask import Flask, render_template

#make the app
app = Flask(__name__)

#make the route
@app.route('/')

#Now define the function
def hello():
    return render_template('home.html')

#make a second route
@app.route("/about")

#now make function that goes with about
def preds():
    return render_template('about.html')
    