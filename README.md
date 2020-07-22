# Spowerfy 

#### Spowerfy is a web application built in Flask that controls the playback of a Spotify playlist to skip to the next song every minute on the minute. It also updates a webpage to show the track name, artist, and album art of the current playback by using an asynchronous background thread.

#### Ideal use case for this web app is to automate your next power hour! :beer:

![demo gif](giphy.gif)

Note: I've sped up the above .gif for illustrative purposes

##### Technologies used:
* Python (async_io, spotipy, Oauth)
* Flask
* JavaScript
* HTML
* CSS 
* Jinja2

This project is based on the very useful Flask-SocketIO code from Miguel Grinberg.

https://github.com/miguelgrinberg/Flask-SocketIO

It is also based on the async_flask code from Shane Lynn:

https://github.com/shanealynn/async_flask

To use - please clone the repository and then set up your virtual environment using the requirements.txt file with pip and virtualenv. You can achieve this with:


    git clone https://github.com/ColemanMitch/Spowerfy
    cd spowerfy
    virtualenv spowerfy
    ./spowerfy/Scripts/activate
    pip install -r requirements.txt  #(or in Windows - sometimes python -m pip install -r requirements.txt )



Start the application with:

<code>
python application.py
</code>

And visit http://localhost:5000 to begin your power hour.
