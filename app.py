import json 
from flask import Flask, render_template
from ordsendpoints import happy2015, happy2016, happy2017, happy2018, happy2019

app =Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')