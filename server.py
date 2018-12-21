#!/usr/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)




import os
def playtune(url):
    os.system('mpsyt playurl ' + url)




@app.route('/', methods=['GET', 'POST'])
def insertTunePage():
    print("Tunepage was requested.")
    if request.method == 'POST':
        url=request.form['url']
        print("Got a post request. Playing url " + url)
        playtune(url)

    return render_template('base.html')
