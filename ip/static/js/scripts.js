$(document).ready(function(){
    $('.dropdown-toggle').dropdown();
    
    console.log("hello, world!");
    var x;
    $.getJSON("https://api.ipify.org?format=jsonp&callback=?",
      function(json) {
        console.log(json);
        x = json.ip;
        $.getJSON("http://ip-api.com/json/" + x, function(json) {
            console.log(json);
        });
      });
        /*error = "";                                             
    $( "#sign-up" ).submit(function() {                     
        if ($('#sign-up input[name=password]').val() != $('#sign-up input[name=password_confirm]').val())
        {
            error = "passwords must match!";
            $("#signup-errors").text(error);
            return false;
        }
        return true;
    });*/
});