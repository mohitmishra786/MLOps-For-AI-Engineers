from bmicalculator import bmi_calculator
from flask import Flask, jsonify, request
import json
# instantiate the flask object
app = Flask('__main__')

@app.route('/', methods =  ['GET', 'POST'])
def get_input():
    '''
    A function to get requests using flask, evluate and return result.
    '''

    packet= request.get_json(force=True)
    weight = packet['weight']
    height = packet['height']

    bmi = bmi_calculator(weight , height)

    return jsonify(packet, bmi)

# driver function
if __name__ == '__main__':
    app.run()
