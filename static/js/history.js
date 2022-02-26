
/***
@Function Open a new window to display a deploy log detail
@Author Jiage
@Date 2021-09-13
***/
function openDetail(id){
    $.ajax({type : 'GET',url:$SCRIPT_ROOT + '/history/detail/'+id,async:false,success:function(result){
          if(!result || result.length === 0){
              $.alert('Not found data! ')
              return
          }
	      var myWindow = window.open("", id, "toolbar=no,status=no,top=500,left=500,width=800,height=500");
	      myWindow.document.write('<title>'+"History Detail by "+id+'</title>')
	      myWindow.document.write("<textarea style='color: white;background-color: black; width: 100%;height: 100%; padding: 0%;'>"+result+"</textarea>")
      }});
}

function openTail(id){
    //send web-socket event to backend service
    var myWindow = window.open("", id, "toolbar=no,status=no,top=500,left=500,width=800,height=500");
	myWindow.document.write('<title>'+"Tracing log real-time by "+id+'</title>')
	myWindow.document.write("<textarea style='color: white;background-color: black; width: 100%;height: 100%; padding: 0%;'>"+result+"</textarea>")
}

function openWeb(id){
    var myWindow = window.open("", id, "toolbar=no,status=no,top=500,left=500,width=800,height=500");
	myWindow.document.write('<title>'+"Open Web by "+id+'</title>')
}

/****
@Function redeploy the service
@Author Jiage
@Date 2021-09-13
***/
function redeploy(id){
    //display prompt window to deploy
    $.confirm({
        title: 'Deploy Confirm',
        content: '' +
        '<form action="" class="formName">' +
        '<div class="form-group">' +
        '<label>Enter Deploy Version Number</label>' +
        '<input type="number" placeholder="Deploy Version Number" class="name form-control" min="1" max="999999" step="1" required />' +
        '</div>' +
        '</form>',
        buttons: {
            formSubmit: {
                text: 'Submit',
                btnClass: 'btn-blue',
                action: function () {
                    var version = this.$content.find('.name').val();
                    if(!version){
                        $.alert('Provide a valid the number of version! ');
                        return false;
                    }
                    //$.alert('Your name is ' + name);
                    deploySubmit(version)
                }
            },
            cancel: function () {
                //close
            },
        },
        onContentReady: function () {
            // bind to events
            var jc = this;
            this.$content.find('form').on('submit', function (e) {
                // if the user submits the form by pressing enter in the field.
                e.preventDefault();
                jc.$$formSubmit.trigger('click'); // reference the button and click it
            });
        }
    });
}

function deploySubmit(version){
     //send web-socket to backend service
}
