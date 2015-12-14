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
    var shared_users_from_form = $("select#id_shared_user").val();
    // convert shared_users objects from modal to array
    shared_users_from_modal = get_keys(shared_users_from_modal);
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
            shared_users_from_form: shared_users_from_form,
            tasks: tasks,
            shared_users_from_modal: shared_users_from_modal
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
    var shared_users_from_form = $("select#id_shared_user").val();
    // tasks is an array
    // username is a string
    // var username = get_username();
    // convert tasks objects to array
    tasks = get_keys(tasks);
    // convert shared_users objects from modal to array
    shared_users_from_modal = get_keys(shared_users_from_modal);

    console.log("edit todo function is working!");
    console.log("text: " + todoText);
    $.ajax({
        url: "",
        type: "POST",
        data: {
            todoTitle: todoTitle,
            todoText: todoText,
            dueDate: dueDate,
            shared_users_from_form: shared_users_from_form,
            tasks: tasks,
            shared_users_from_modal: shared_users_from_modal
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

function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function checkIfFriend(email) {
    return $.ajax({
        url: "/todo/check_email/",
        type: "POST",
        data: {
            email: email
        }

        /*success : function(json) {
            debugger;
            console.log(json);
            console.log("email is friends with user!");
            return true;
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            debugger;
            console.log(json);
            console.log("email isn't user or email isn't friends with user :(");
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            return false;
        }*/
    });
}

function deleteTaskFromTodo(task_pk) {
    $.ajax({
        url: "/todo/delete_task/" + task_pk + "/",
        type: "POST",
        data: {
            task_pk: task_pk
        },

        success : function(json) {
            console.log(json);
            console.log("js says success on task delete!!");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(json);
            console.log("js says u failed to delete task :(");
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


function get_num(numsAndLetters) {
    return numsAndLetters.replace( /^\D+/g, '');
}


function deleteSharedUserFromTodo(weird_user_id) {
    var todo_pk = $('.todo-pk').text().trim();
    var user_id = get_num(weird_user_id);
    $.ajax({
        url: "/todo/delete_shared_user/",
        type: "POST",
        data: {
            user_id: user_id,
            todo_pk: todo_pk
        },

        success : function(json) {
            console.log(json);
            console.log("js says success on shared_user delete!!");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(json);
            console.log("js says u failed to shared_user delete :(");
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


function complete_task() {
    //complete task when x badge is clicked on to-do detail for incomplete tasks
    $(document).on('click', '.todo-detail-incomplete', function () {
        task_pk = this.id;
        console.log("complete task button clicked for " + task_pk);
        
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
}

function incomplete_task() {
    //incomplete task when x badge is clicked on to-do detail for complete tasks
    $(document).on('click', '.todo-detail-complete', function () {
        task_pk = this.id;
        console.log("incomplete task button clicked for " + task_pk);
        
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
}


function delete_task() {
    // delete task when X badge is clicked
    $(document).on('click', '.add-form', function () {
        console.log("delete button clicked for " + this.id);
        // remove li from ul
        $("#" + this.id).remove();
        //call django to delete task from database
        if (!(this.id in tasks)) {
            deleteTaskFromTodo(this.id);
        }
        // remove task from array of tasks
        delete tasks[this.id];
    });
}

function add_task() {
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
            $('ul.added-tasks-in-form').append("<li class='list-group-item' id='"+i+"' ><span class='badge add-form' id='"+i+"' >X</span>" + taskDescription + "</li>");
            i++;
        }
        
    });
}

function add_shared_user_to_todo() {
    // get modal button that adds a shared user
    // get email user has entered
    // check if for blankness
    // check to see if it's a properly formatted email address
    // add to list of emails to send to django
    // add email to modal with option to delete
    $("#modal-add-shared-user-button").click(function(event){
        var sharedUserEmail = $("#shared-user-email").val();
        console.log("shared user button clicked!!");
        console.log(sharedUserEmail);
        // reject if blank
        var validEmail = validateEmail(sharedUserEmail);
        // reject if not a friend with user
        var promise = checkIfFriend(sharedUserEmail);
        if (sharedUserEmail == "" || !validEmail) {
            console.log("error with email!");
            // print some error to the form ideally

            /*$("div#task.input-group").addClass("input-group has-error");*/
        } else {
            promise.success(function (data){
                var friendsWithUser = data;
                if (friendsWithUser != "valid email and users are friends") {
                    console.log("invalid email or users aren't friends :(");
                    //print some error to the form ideally
                } else {
                    //unhide hidden label
                    $("div.shared-users").addClass("unhidden");
                    $("div.shared-users").removeClass("hidden");
                    // undo error input box
                    $("div#task").removeClass("input-group has-error");
                    $("div#task").addClass("input-group");
                    // else save the value to some data structure
                    shared_users_from_modal["shared" + i] = sharedUserEmail;
                    console.log(shared_users_from_modal);
                    // clear the contents of test-description text box
                    $("#shared-user-email").val("");
                    // add html div with task description
                    $('ul.shared-user-list').append("<li class='list-group-item' id='shared"+j+"' ><span class='badge add-form-shared-user' id='shared"+j+"' >X</span>" + sharedUserEmail + "</li>");
                    j++;
                }
            });
        }
        
    });
}

function delete_shared_user_from_todo() {
    // delete shared email when X badge is clicked in modal
    $(document).on('click', '.add-form-shared-user', function () {
        console.log("delete button clicked for " + this.id);
        // remove li from ul
        $("#" + this.id).remove();
        if (!(this.id in shared_users_from_modal)) {
            deleteSharedUserFromTodo(this.id);
        }
        // remove task from array of tasks
        delete shared_users_from_modal[this.id];
    });
}

function submit_edited_todo() {
    $('form#edit-todo-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        edit_todo(tasks, shared_users_from_modal);
    });
}


tasks = {};
shared_users_from_modal = {};
i = 0;
j = 0;

$(document).ready(function() {
    // in edit_todo_form
    // toggle complete/incomplete tasks
    // add new tasks
    complete_task(); // edit-form
    incomplete_task(); // edit-form
    add_task(); // edit-form & add-form
    submit_edited_todo(); // edit-form
    //put modal code in seperate section
    delete_task(); // edit form $ add-form
    add_shared_user_to_todo(); // edit-form & add-form
    delete_shared_user_from_todo(); // edit-form & add-form

    // send all tasks to django when add todo form submitted
    // TODO - CHECK FORM BEFORE SUBMISSION!
    $('form#todo-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        create_todo(tasks, shared_users_from_modal);
    });

    // send all tasks to django when edit todo form submitted
    // TODO - CHECK FORM BEFORE SUBMISSION!




    // handle modal submission on edit and add form
    $("#myModal").on("hidden.bs.modal", function() {
        console.log("Modal clicked!");
    });

    $('#modal-submit').click(function(){
         /* when the submit button in the modal is clicked, submit the form */
        console.log('submitting');
        
    });

});
