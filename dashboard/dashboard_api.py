from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/threats")
def get_threats():
    try:
        with open("threats_log.json") as f:
            return jsonify(json.load(f))
    except:
        return jsonify([])

app.run(port=5000)