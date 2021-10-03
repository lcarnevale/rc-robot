# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
This implementation does its best to follow the Robert Martin's Clean code  guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

actions = [
    "move forward",
    "move backward",
    "turn right",
    "turn left"
]

"""
    Num     Action
    0       move forward
    1       move backward
    2       turn right
    3       turn left
"""
@app.get("/robots/<robot_id>/actions/<action_id>")
def move(robot_id, action_id):
    action_id = int(action_id)
    print("do action %s" % (actions[action_id]))
    return "", 201
    # return {"error": "Request must be JSON"}, 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)