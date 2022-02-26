//response
socket.on('response', function(msg) {
    //process the event of system
    if(msg.event == 'connect'){
       log("The console's status connection is "+msg.data);
       //process the event of log
    }else if(msg.event == 'log-deploy'){
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
     if($("#log-deploy").val().length > 0){
         var s = $("#log-deploy").val() + '\n';
         v = s + v;
     }
     $("#log-deploy").val(v);
     $("#log-deploy").scrollTop( $("#log-deploy")[0].scrollHeight - $("#log-deploy").height() );
}
function clear(){
   $('#log-deploy').val('');
}

function query(){
   clear()
   $("#queryStatus").text("   querying...")
   socket.emit('request', {event: 'query_deploy', data: ""})
}

