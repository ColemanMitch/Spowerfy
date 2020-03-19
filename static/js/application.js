
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var tracks_received = [];
    var artists_received = [];
    var counter;
    var album_art_url = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log(msg.counter + "Received track " + msg.number + " by "+ msg.artist + " album url = " + msg.url);
        //maintain a list of ten numbers
        if (tracks_received.length >= 1){
            tracks_received.shift()
        }      
        if (artists_received.length >= 1){
            artists_received.shift()
        }       
        if (album_art_url.length >= 1){
            album_art_url.shift()
        }     

        tracks_received.push(msg.number);
        artists_received.push(msg.artist);
        album_art_url.push(msg.url);
        counter = msg.counter;

        numbers_string = '';
        artists_string =''; 
        album_art_url_string = "";


        for (var i = 0; i < tracks_received.length; i++){
            numbers_string = numbers_string.concat('<h4>', counter.toString() , ': "', tracks_received[i].toString(), '" by ', artists_received[i].toString(),'</h4>');
            album_art_url_string = album_art_url_string.concat('<img src= ', album_art_url[i].toString(), ' alt="Album Art" class="center" height = "500" width="500" >');
        }
        $('#log').html(numbers_string);
        $('#album').html(album_art_url_string);

    });

});