from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', nome='inicio galera')

@app.route('/contatos')
def contato():
    return render_template('contatos.html')