from flask import Flask, request, jsonify
from replit import db

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/input')
def input():
  col = request.args.get('color')
  num = request.args.get('number')
  lst = [col, num]
  db['col'] = col
  db['num'] = num
  return jsonify(lst)

@app.route('/output')
def output():
  color = db['col']
  num = db['num']
  lst = [color, num]
  return jsonify(lst)

app.run(host='0.0.0.0', port=8080)
