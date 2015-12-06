tasks = [];


$(document).ready(function() {

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
        
        // send all tasks to django when form submitted
    });

});