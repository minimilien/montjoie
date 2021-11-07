# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:02:11 2021

@author: minimilien
"""
from flask import Flask, render_template,request,redirect,url_for
import webbrowser
from product import load_products


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/home')
def home():
    return render_template(
        'home.html',
        products=load_products()
    )


@app.route('/', methods=['POST'])
def submit():
    val = request.form.to_dict()
    print(val)
    return render_template(
        'index.html'
    )


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return redirect(url_for('index'))


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/home', new=2)
    print("Lancement de l'app")
    app.run(threaded=True)