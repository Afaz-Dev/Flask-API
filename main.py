from flask import Flask, request, jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/api/message', methods=['POST'])
def receiveshit() :
  content = request.get_json()
  print("textc", content['textc'])
  print("messagecode", content['messagecode'])
  return {"response" : "it works!"}


app.run(host='0.0.0.0', port=81)
