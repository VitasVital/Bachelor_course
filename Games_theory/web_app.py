#!flask/bin/python
from flask import Flask, jsonify, request, Response, abort
from flask_cors import CORS, cross_origin
import Games_theory_3 as gm3
import random as rn

app = Flask(__name__)
CORS(app)

@app.route('/todo/api/v1.0/get_k', methods=['POST'])
def get_k():
    result = gm3.get_all_K_json(int(request.json['N']))
    return jsonify(result)

@app.route('/todo/api/v1.0/get_v_k', methods=['POST'])
def get_v_k():
    V_k = request.json['V_k']
    N = int(request.json['N'])
    result = gm3.get_all_v_K_json(N, V_k.split())
    return jsonify(result)

@app.route('/todo/api/v1.0/get_random_v_k', methods=['POST'])
def get_random_v_k():
    N = int(request.json['N'])
    result = gm3.get_all_random_v_K_json(N)
    return jsonify(result)

@app.route('/todo/api/v1.0/find_sheply', methods=['POST'])
def find_sheply():
    N = int(request.json['N'])
    V_k = request.json['V_k']
    V_k = V_k.split()
    V_k_int = [int(x) for x in V_k]
    result = gm3.find_Sheply(N, V_k_int)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)