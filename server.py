#!/usr/bin/python3

from flask import Flask, render_template, request # For server stuff
import subprocess # For doing mpyt stuff

app = Flask(__name__)

import os     #For killing process
import signal #For killing process
import pafy
import vlc


dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, 'pid.txt')

#
# Functionality functions
#
def execute_action(data):
    if data['action'] == "play":
        playtune(data['url'])
    elif data['action'] == "toggle":
        togglePlayPause()
    elif data['action'] == "volume":
        print('ok')
        setVolume(data['volume'])

def setVolume(volume):
    os.system('vlc-ctrl volume ' + volume + '%')


def togglePlayPause():
    os.system('vlc-ctrl toggle')

def playtune(url):
    #Kill process that was running
    os.system('vlc-ctrl quit')

    #Start new instance
    #The following is SUPER unsafe but oh well.
    #It also doesn't work bc killing mpsyt doesn't end the video apparently bc that runs in VLC...
    #Find a way to kill a running process but only if it's mpyt.
    print("executing: "+'mpsyt playurl '+url)
    os.system('mpsyt playurl '+url)



#
# Routes
#
@app.route('/', methods=['GET', 'POST'])
def insertTunePage():
    print("Tunepage was requested.")
    if request.method == 'POST':
        execute_action(request.form)

    return render_template('index.html')
