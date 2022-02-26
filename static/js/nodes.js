//response
socket.on('response', function(msg) {
    //process the event of system
    if(msg.event == 'connect'){
       log("The console's status connection is "+msg.data);
       //process the event of log
    }else if(msg.event == 'log-nodes'){
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
     if($("#log-nodes").val().length > 0){
         var s = $("#log-nodes").val() + '\n';
         v = s + v;
     }
     $("#log-nodes").val(v);
     $("#log-nodes").scrollTop( $("#log-nodes")[0].scrollHeight - $("#log-nodes").height() );
}
function clear(){
   $('#log-nodes').val('');
}

function query(){
   clear()
   $("#queryStatus").text("   querying...")
   socket.emit('request', {event: 'query_nodes', data: ""})
}

