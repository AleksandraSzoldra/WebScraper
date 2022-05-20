from app import app
from flask import render_template

@app.route('/')
@app.route('/index/<name>')
def index(name="Hello World"):
   return render_template('index.html', text=name)

@app.route('/something')
def something():
    return 'Aleksandra Szoldra' 
