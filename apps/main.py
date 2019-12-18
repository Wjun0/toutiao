
from flask import Flask, jsonify
from apps import create_app

app = create_app('dev')


@app.route('/')
def route_map():
    return jsonify({rule.endpoint:rule.rule
                    for rule in app.url_map.iter_rules()})
