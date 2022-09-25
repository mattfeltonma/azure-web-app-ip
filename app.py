import logging
import json
import requests
import os
from flask import Flask, render_template, request, redirect

# Setup up a Flask instance
app = Flask(__name__)


# Render the template
@app.route("/")
def index():
    # Get source IP and headers
    if 'X-Forwarded-For' in request.headers:
        X_FORWARDED_FOR = request.headers['X-Forwarded-For']
    else:
        X_FORWARDED_FOR = 'Empty'
    if 'X-Forwarded-Host' in request.headers:
        X_FORWARDED_HOST = request.headers['X-Forwarded-Host']
    else:
        X_FORWARDED_HOST = 'Empty'
    if 'X-Forwarded-Port' in request.headers:
        X_FORWARDED_PORT = request.headers['X-Forwarded-Port']
    else:
        X_FORWARDED_PORT = 'Empty'
    SOURCE_IP_ADDRESS = request.remote_addr
    HEADERS = json.dumps(dict(request.headers), sort_keys = True, indent = 4, separators = (',', ': '))
    return render_template('index.html', xfor=X_FORWARDED_FOR, xhost=X_FORWARDED_HOST, xport=X_FORWARDED_PORT, sip=SOURCE_IP_ADDRESS, headers=HEADERS)
