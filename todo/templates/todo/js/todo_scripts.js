// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function get_username() {
    var url = window.location.href;
    var urlLength = url.length;
    var first_slash = url.indexOf("do/") + 3;
    var username = url.slice(first_slash, -5)
    return username;
}

function create_todo(tasks) {
    // tastTitle is a string
    var taskTitle = $("#id_title").val();
    // taskText is a string
    var taskText = $("#id_text").val();
    // dueDate is a string
    var dueDate = $("input#yourdatetimeid").val();
    // shared_users is an array
    var shared_users = $("select#id_shared_user").val();
    // tasks is an array
    // username is a string
    var username = get_username();

    console.log("create todo function is working!");
    console.log("text: " + taskText);
    $.ajax({
        url: "todo/" + username + "/add/",
        type: "POST",
        data: {
            taskTitle: taskTitle,
            taskText: taskText,
            dueDate: dueDate,
            shared_users: shared_users,
            username: username
        }

        success : function(json) {
            // redirect to todo_detail
        }
    })
}


tasks = [];


$(document).ready(function() {

    // send all tasks to django when form submitted
    $('form#todo-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_todo(tasks);
    });

    // get task button when clicked!
    $("#task-button").click(function(event){
        var taskDescription = $("#task-description").val();
        console.log("button clicked!");
        console.log(taskDescription);
        // reject if blank
        if (taskDescription == "") {
            console.log("it's blank!");
            $("div#task.input-group").addClass("input-group has-error");
        } else {
            //unhide hidden label
            $("div.hidden").addClass("unhidden");
            $("div.hidden").removeClass("hidden");
            // undo error input box
            $("div#task").removeClass("input-group has-error");
            $("div#task").addClass("input-group");
            // else save the value to some data structure
            tasks.push(taskDescription);
            console.log(tasks);
            // clear the contents of test-description text box
            $("#task-description").val("");
            // add html div with task description
            $('ul.list-group').append('<li class="list-group-item">' + taskDescription + '</li>');
        }
        
    });

});
