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
        setVolume(data['volume'])
    elif data['action'] == "stop":
        closePlayer()

def setVolume(volume):
    newvol=str(int(volume)+20)
    os.system('vlc-ctrl volume ' + newvol + '%')

def togglePlayPause():
    os.system('vlc-ctrl toggle')

def playtune(url):
    #Kill process that was running
    closePlayer()

    #Start new instance
    print("executing: "+'mpsyt playurl '+url)
    os.system('mpsyt playurl '+url)

def closePlayer():
    os.system('vlc-ctrl quit')


#
# Routes
#
@app.route('/', methods=['GET', 'POST'])
def insertTunePage():
    print("Tunepage was requested.")
    if request.method == 'POST':
        execute_action(request.form)

    return render_template('index.html')
