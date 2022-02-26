//response
socket.on('response', function(msg) {
    //process the event of system
    if(msg.event == 'connect'){
       log("The console's status connection is "+msg.data);
       //process the event of log
    }else if(msg.event == 'log-cluster'){
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
     if($("#log-cluster").val().length > 0){
         var s = $("#log-cluster").val() + '\n';
         v = s + v;
     }
     $("#log-cluster").val(v);
     $("#log-cluster").scrollTop( $("#log-cluster")[0].scrollHeight - $("#log-cluster").height() );
}
function clear(){
   $('#log-cluster').val('');
}

function query(){
   clear()
   $("#queryStatus").text("   querying...")
   socket.emit('request', {event: 'query_cluster', data: ""})
}

