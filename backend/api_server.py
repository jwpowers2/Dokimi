#!/usr/bin/python
import json
import math
from flask import Flask, request
from flask_cors import CORS, cross_origin
from .RecursionString import RecursionString

app = Flask(__name__)
CORS(app)

# produces are of a triangle


@app.route('/api/area', methods=['POST'])
@cross_origin()
def get_area():
    data = json.loads(request.data.decode('latin1'))
    # need to see which operation to perform
    one = data['sideOne']
    two = data['sideTwo']
    three = data['sideThree']
    angle = data['angleOfIntersection']
    if (three):
        # use heron's formula
        p = (one + two + three) / 2
        print(p)
        heron = p * (p - one) * (p - two) * (p - three)
        print(heron)
        area = math.sqrt(heron)
        print(area)
        return str(area)
    else:
        # here deal with where you know two sides and an angle
        area = .5 * one * two * (math.sin(angle))
        return str(area)

# produces max edge of triangle, given two sides


@app.route('/api/maxedge', methods=['POST'])
@cross_origin()
def get_maxedge():
    data = json.loads(request.data.decode('latin1'))
    int_one = data['intOne']
    int_two = data['intTwo']

    if (type(int_one) == int and type(int_two) == int):
        max_edge = (int_one + int_two) - 1
        return json.dumps(max_edge)
    else:
        return "error with operation", 400

# produces seconds from hours/minutes


@app.route('/api/seconds', methods=['POST'])
@cross_origin()
def get_seconds():
    data = json.loads(request.data.decode('latin1'))
    hours = data['hours']
    if not hours:
        h = 0
    else:
        h = hours
    minutes = data['minutes']
    if not minutes:
        m = 0
    else:
        m = minutes
    seconds = (m * 60) + (h * 3600)
    return json.dumps(seconds)

# produces string of messages recursively


@app.route('/api/recursion', methods=['POST'])
@cross_origin()
def get_strings():
    data = json.loads(request.data.decode('latin1'))
    # use message and count
    my_list = RecursionString().rec_string(data['message'], data['count'])
    return ' '.join(my_list)
