Spowerfy 

Cole Mitchell 03/19/2020

===========

![demo gif](giphy.gif)
Note: I've sped up the playback in the above .gif for illustrative purposes

Test of asynchronous flask communication with web page. 

Spowerfy is a flask application that controls the playback of a Spotify playlist and updates a webpage to the album art of the track that is currently playing by using a background thread for all users connected.

It is based on the very useful Flask-SocketIO code from Miguel Grinberg.

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
