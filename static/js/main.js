function call(){
    var name = $.trim( $('#name').val());
    var email = $.trim( $('#email').val());
    var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
    alert(csrfmiddlewaretoken);

        $.ajax({

            type: "POST",
            async: false,
            url: '/user/create/',
            data: 'name=' + name+'&email='+email+'&csrfmiddlewaretoken='+csrfmiddlewaretoken,
            cache: false,

            success: function(result) {

            console.log(result);

        }

        }) //function closed for sending data into database
}