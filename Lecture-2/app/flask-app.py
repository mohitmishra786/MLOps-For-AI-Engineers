from bmicalculator import bmicalculator
from flask import Flask, jsonify, request

# instantiate the flask object
app = Flask{}

@app.route('/', methods =  ['GET', 'POST'])

