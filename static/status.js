//response
socket.on('response', function(msg) {
    //process the event of system
    if(msg.event == 'connect'){
       log("The console's status connection is "+msg.data);
       //process the event of log
    }else if(msg.event == 'log-status'){
       log(msg.data)
       //process error
    }else{
       log("Error: response a wrong message. event: "+msg.event+" message: "+ msg.data);
    }
});
/**
* Log a text message
* @param {String} txt
*/
function log(v) {
     $("#queryStatus").text("")
     if($("#log-status").val().length > 0){
         var s = $("#log-status").val() + '\n';
         v = s + v;
     }
     $("#log-status").val(v);
     $("#log-status").scrollTop( $("#log-status")[0].scrollHeight - $("#log-status").height() );
}
function clear(){
   $('#log-status').val('');
}

function query(){
   clear()
   $("#queryStatus").text("   querying...")
   socket.emit('request', {event: 'query_status', data: ""})
}

