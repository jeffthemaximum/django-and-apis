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
    var username = url.slice(first_slash, -4);
    return username;
}

function get_keys(dict) {
    keys = [];
    for(var key in dict) {
        keys.push(dict[key]);
    }
    return keys;
}

function create_todo(tasks) {
    // tastTitle is a string
    var todoTitle = $("#id_title").val();
    // taskText is a string
    var todoText = $("#id_text").val();
    // dueDate is a string
    var dueDate = $("input#yourdatetimeid").val();
    // shared_users is an array
    var shared_users = $("select#id_shared_user").val();
    // tasks is an array
    // username is a string
    // var username = get_username();
    // convert tasks objects to array
    tasks = get_keys(tasks);

    console.log("create todo function is working!");
    console.log("text: " + todoText);
    $.ajax({
        url: "",
        type: "POST",
        data: {
            todoTitle: todoTitle,
            todoText: todoText,
            dueDate: dueDate,
            shared_users: shared_users,
            tasks: tasks
        },

        success : function(json) {
            console.log(json);
            console.log("success!");
            location.href = json.redirect;

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function edit_todo(tasks) {
    // tastTitle is a string
    var todoTitle = $("#id_title").val();
    // taskText is a string
    var todoText = $("#id_text").val();
    // dueDate is a string
    var dueDate = $("input#yourdatetimeid").val();
    // shared_users is an array
    var shared_users = $("select#id_shared_user").val();
    // tasks is an array
    // username is a string
    // var username = get_username();
    // convert tasks objects to array
    tasks = get_keys(tasks);

    console.log("edit todo function is working!");
    console.log("text: " + todoText);
    $.ajax({
        url: "",
        type: "POST",
        data: {
            todoTitle: todoTitle,
            todoText: todoText,
            dueDate: dueDate,
            shared_users: shared_users,
            tasks: tasks
        },

        success : function(json) {
            console.log(json);
            console.log("success!");
            location.href = json.redirect;

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


tasks = {};


$(document).ready(function() {
    var i = 0;

    //complete task when x badge is clicked on to-do detail for incomplete tasks
    $(document).on('click', '.todo-detail-incomplete', function () {
        task_pk = this.id;
        console.log("delete button clicked for " + task_pk);
        
        // ajax call to set it to complete
        $.ajax({
            url: "/todo/task_complete/" + task_pk + "/",
            type: "POST",
            data: {
                task_pk: this.id
            },

            success : function(json) {
                console.log(json);
                console.log("success!");
                //get task title
                var task_title = $('#incomplete-li' + task_pk).text().substr(1);
                // jquery to move it to complete section
                $(".complete-task-list").append(
                    "<li class='list-group-item' id='complete-li"+task_pk+"'><span class='badge todo-detail-complete' id='"+task_pk+"' >X</span>"+task_title+"</li>"
                );
                $("#incomplete-li"+task_pk).remove();
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });

    //incomplete task when x badge is clicked on to-do detail for complete tasks
    $(document).on('click', '.todo-detail-complete', function () {
        task_pk = this.id;
        console.log("delete button clicked for " + task_pk);
        
        // ajax call to set it to complete
        $.ajax({
            url: "/todo/task_incomplete/" + task_pk + "/",
            type: "POST",
            data: {
                task_pk: this.id
            },

            success : function(json) {
                console.log(json);
                console.log("success!");
                //get task title
                var task_title = $('#complete-li' + task_pk).text().substr(1);
                // jquery to move it to complete section
                $(".incomplete-task-list").append(
                    "<li class='list-group-item' id='incomplete-li"+task_pk+"'><span class='badge todo-detail-incomplete' id='"+task_pk+"' >X</span>"+task_title+"</li>"
                );
                $("#complete-li" +task_pk).remove();
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });


    // delete task when X badge is clicked
    $(document).on('click', '.add-form', function () {
        console.log("delete button clicked for " + this.id);
        // remove li from ul
        $("#" + this.id).remove();
        // remove task from array of tasks
        delete tasks[this.id];
    });

    // send all tasks to django when add todo form submitted
    // TODO - CHECK FORM BEFORE SUBMISSION!
    $('form#todo-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        create_todo(tasks);
    });

    // send all tasks to django when edit todo form submitted
    // TODO - CHECK FORM BEFORE SUBMISSION!
    $('form#edit-todo-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        edit_todo(tasks);
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
            tasks[i] = taskDescription;
            console.log(tasks);
            // clear the contents of test-description text box
            $("#task-description").val("");
            // add html div with task description
            $('ul.list-group').append("<li class='list-group-item' id='"+i+"' ><span class='badge add-form' id='"+i+"' >X</span>" + taskDescription + "</li>");
            i++;
        }
        
    });

    // handle modal submission on edit and add form
    $("#myModal").on("hidden.bs.modal", function() {
        console.log("Modal clicked!");
    });

    $('#modal-submit').click(function(){
         /* when the submit button in the modal is clicked, submit the form */
        console.log('submitting');
        
    });

});
