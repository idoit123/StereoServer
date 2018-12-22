#!/usr/bin/python3

from flask import Flask, render_template, request # For server stuff
import subprocess # For doing mpyt stuff

app = Flask(__name__)

import os     #For killing process
import signal #For killing process

dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, 'pid.txt')

def playtune(url):
    #The following is SUPER unsafe but oh well.
    #It also doesn't work bc killing mpsyt doesn't end the video apparently bc that runs in VLC...
    #Find a way to kill a running process but only if it's mpyt.
    #Kill process that was running
    f=open(filepath, "r")
    prev_pid=int(f.read())
    print(str(prev_pid))
    try:
        os.kill(prev_pid, signal.SIGTERM) #or signal.SIGKILL idk
    except ProcessLookupError:
        print("Oops I tried to kill a process that doesn't exist :*")

    #Start new instance
    proc = subprocess.Popen(["mpsyt", "playurl", url], shell=False)

    #Save pid
    file=open(filepath, "w")
    file.write(str(proc.pid))


@app.route('/', methods=['GET', 'POST'])
def insertTunePage():
    print("Tunepage was requested.")
    if request.method == 'POST':
        url=request.form['url']
        print("Got a post request. Playing url " + url)
        playtune(url)

    return render_template('base.html')
