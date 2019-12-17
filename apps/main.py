
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def route_map():
    return jsonify({rule.enddpoint:rule.rule
                    for rule in app.url_map.iter_rules()})
