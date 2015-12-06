

$(document).ready(function() {

    // get task button when clicked!
    $("#task-button").click(function(event){
        var taskDescription = $("#task-description").val();
        console.log("button clicked!");
        console.log(taskDescription);
        // reject if blank
        // else save the value to some data structure
        // clear the contents of test-description text box
        // add html div with task description
        // send all tasks to django when form submitted
    });

});