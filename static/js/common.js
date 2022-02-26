
//websocket
var socket = io();
//connect
socket.on('connect', function() {
    socket.emit('request', {event: 'connect', data: 'I\'m connected!'});
});