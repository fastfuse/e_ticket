
# -*- coding: utf-8 -*-

import json
import requests
from app import app
from flask import request, url_for, redirect, render_template, jsonify


ROOT_URL = 'http://api.genius.com/'
SEARCH_URL = ROOT_URL + 'search?'   # r.get(url, params=search_params)
HEADERS = {'Authorization': 'Bearer g3I0_dpr-oZRNdnLowg1uT7VznFugwXEZpFsBVExX6f-K7V2QUMiKBOxqoIVtxNs'}


def _requests_get(url):
    r_obj = requests.get(url)
    fixed_obj = json.loads(r_obj.json())

    return fixed_obj


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/ping')
def ping():
    print(request.args.get('q', None))

    search_query = request.args.get('q', None)

    url = SEARCH_URL + 'q=' + search_query

    r = requests.get(url, headers=HEADERS)
    print(r.json().keys())

    return jsonify(r.json())
