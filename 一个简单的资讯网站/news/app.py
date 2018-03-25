#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from flask import Flask, render_template
import jinja2
import json

app = Flask(__name__)

@app.route('/')
def index():
    jsonl = []
    path = '/home/shiyanlou/files'
    dirs = os.listdir(path)
    for i in dirs:
        if os.path.splitext(i)[1] == ".json":
            jsonl.append(i)
    return render_template('index.html', jsonl=jsonl)

@app.route('/files/<filename>')
def file(filename):
    pathf = os.path.join('/home/shiyanlou/files', filename+'.json')
    if os.path.exists(pathf):
        f = open(pathf, encoding='utf-8')
        content = json.load(f)
        return render_template('file.html', content=content)
    else:
        return render_template('404.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True)
