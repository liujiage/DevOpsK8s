//response
socket.on('response', function(msg) {
    //process the event of system
    if(msg.event == 'connect'){
       log("The console's status connection is "+msg.data);
       //process the event of log
    }else if(msg.event == 'log-services'){
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
     if($("#log-services").val().length > 0){
         var s = $("#log-services").val() + '\n';
         v = s + v;
     }
     $("#log-services").val(v);
     $("#log-services").scrollTop( $("#log-services")[0].scrollHeight - $("#log-services").height() );
}
function clear(){
   $('#log-services').val('');
}

function query(){
   clear()
   $("#queryStatus").text("   querying...")
   socket.emit('request', {event: 'query_services', data: ""})
}

