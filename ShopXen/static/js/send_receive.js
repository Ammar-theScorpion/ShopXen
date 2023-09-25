$(document).ready(function() {
    var ajax = null;
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    console.log(csrftoken);

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
           if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
               xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
     }
  });
  $('#delete').click(function(event){
    event.preventDefault()
    //tname = 'reverseString';
    if(ajax !== null){
        return;
    }
    ajax = $.ajax({
        url: 'http://127.0.0.1:8000/delchat',
            method:'POST',
            contentType: 'text/plain', // to prevent Django from treating the ajax as a form form the Query
            error:function(e){
                console.log(e)
            },
            success: function(response){
                $('#chat').text ('')
            },
            complete: function(){
                ajax = null;
            }
        
        });
});
    $('#query').click(function(event){
        event.preventDefault()
        $('#chat').text ('')

        text = document.getElementById('input').value;
        //tname = 'reverseString';
        if(ajax !== null){
            return;
        }
        ajax = $.ajax({
            url: 'http://127.0.0.1:8000/chat',
                method:'POST',
                contentType: 'text/plain', // to prevent Django from treating the ajax as a form form the Query
                data: {
                   
                    'query': text,
                },
                error:function(e){
                    console.log(e)
                },
                success: function(response){
                    try{

                        var entries = response.split("@");
                        console.log(entries)
                        for (var i = 0; i < entries.length-1; i+=3) {

                            var user = entries[i];
                            var bot = entries[i+1]
                            let h3 = $("<h3>").text('user: '+user);
                            
                            $("#chat").append(h3); 
                            h3 = $("<h3>").text('bot: '+bot);
                            $("#chat").append(h3); 
                            console.log("User: " + user);
                            console.log("Bot: " + bot);
                        }
                    }catch(e){}
                },
                complete: function(){
                    ajax = null;
                }
            
            });
    });
});