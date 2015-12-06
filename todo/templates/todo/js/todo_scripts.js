$(document).ready(function() {

    // get task button when clicked!
    $("#task-button").click(function(event){
        console.log("button clicked!");
        console.log($("#task-description").val());
    });

});