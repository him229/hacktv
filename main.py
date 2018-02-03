from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/msg', methods=['GET', 'POST'])
def get_terminal():
    return json.dumps({"msg": 'good'})

@app.route('/')
def index():
    return "It's working"

if __name__ == '__main__':
    app.run(port=11111)