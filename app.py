#!/usr/bin/env python3
"""
Simple Echo Service
A basic Flask application that echoes back the input
"""

from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Echo Service</h1>
    <p>This is a simple echo service that returns whatever you send to it.</p>
    <p>Try: <code>curl -X POST -H "Content-Type: application/json" -d '{"message":"Hello World"}' http://localhost:5000/echo</code></p>
    '''

@app.route('/echo', methods=['POST'])
def echo():
    """
    Echo endpoint that returns the received data
    """
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({
                'error': 'No JSON data provided',
                'received': None
            }), 400
        
        response = {
            'original_request': data,
            'echo': data,
            'message': 'Echo service received your data successfully'
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Error processing request'
        }), 500

@app.route('/echo', methods=['GET'])
def echo_info():
    """
    GET method for echo endpoint - provides information about the service
    """
    return jsonify({
        'service': 'Echo Service',
        'method': 'GET',
        'description': 'This is an echo service. Send a POST request with JSON data to get it echoed back.',
        'example': {
            'endpoint': '/echo',
            'method': 'POST',
            'body': {'message': 'Hello World'}
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)