"""
Flask application that controls the playback of a Spotify playlist and dynamically updates a webpage based on the current track using socket.io

19th March 2020

"""


# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

__author__ = ''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)
cid = '[INPUT YOUR CLIENT ID HERE]'
secret = '[INPUT YOUR CLIENT SECRET HERE]'
scope = 'user-read-playback-state,user-modify-playback-state'
user = '[INPUT YOUR USER # HERE]'
uri = 'http://localhost/'

interval = 60

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=cid, client_secret = secret, redirect_uri = uri, scope=scope, username=user))


thread = Thread()
thread_stop_event = Event()

def powerHour():
    """
    Generate the next track every interval
    """
    #infinite loop of magical random numbers
    print("Generating a güd time :)")
    sp.start_playback(device_id='[INPUT YOUR DEVICE ID HERE]',context_uri='s[INPUT YOUR PLAYLIST URI HERE]')
    counter = 1

    while not thread_stop_event.isSet():
        sp.next_track()
        sleep(1)
        current_song = sp.current_playback()
        track = current_song['item']['name']
        artist = current_song['item']['album']['artists'][0]['name']
        album_url = current_song['item']['album']['images'][0]['url']

        print(counter)
        print(track)
        pprint(artist)
        pprint(album_url)

        socketio.emit('newnumber', {'number': track, 'artist': artist, 'counter': counter, 'url': album_url }, namespace='/test')
        counter = counter+1
        socketio.sleep(interval-1)


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.is_alive():
        #print("Starting Thread")
        thread = socketio.start_background_task(powerHour)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
