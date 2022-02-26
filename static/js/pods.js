//response
socket.on('response', function(msg) {
    //process the event of system
    if(msg.event == 'connect'){
       log("The console's status connection is "+msg.data);
       //process the event of log
    }else if(msg.event == 'log-pods'){
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
     if($("#log-pods").val().length > 0){
         var s = $("#log-pods").val() + '\n';
         v = s + v;
     }
     $("#log-pods").val(v);
     $("#log-pods").scrollTop( $("#log-pods")[0].scrollHeight - $("#log-pods").height() );
}
function clear(){
   $('#log-pods').val('');
}

function query(){
   clear()
   $("#queryStatus").text("   querying...")
   socket.emit('request', {event: 'query_pods', data: ""})
}

