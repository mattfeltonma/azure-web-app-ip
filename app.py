from email import header
import logging
import json
import requests
import os
from flask import Flask, render_template, request, redirect

# Setup up a Flask instance
app = Flask(__name__)

# These headers are placed in the table
display_headers = [
    "X-Forwarded-For",
    "X-Client-Ip",
    "X-Forwarded-Port",
    "X-Client-Port",
    "X-Forwarded-Proto",
    "X-Forwarded-Host"
]

# Render the template
@app.route("/")
def index():

    # Iterate through the dict of headers to highlight and set the value equal
    active_headers = {}
    for header_name in display_headers:
        if header_name in request.headers:
            active_headers[header_name] = request.headers[header_name]


    # Capture the source IP of the request and all headers in the request to display later on
    active_headers['CLIENT IP'] = request.remote_addr
    HEADERS = json.dumps(dict(request.headers), sort_keys = True, indent = 4, separators = (',', ': '))

    # Build an HTML table with the headers that you want displayed



    return render_template('index.html', headers=HEADERS, active_headers=active_headers)
