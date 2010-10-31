$(document).ready(function() {
    $(".errorlist").hide().fadeIn("slow");
    $(".messages").hide().fadeIn("slow");

    $(function() {
        $(".date-field").datepicker({
            dateFormat: 'yy-mm-dd'
        });
    });

    $(".delete-button").click(function() {
        var has_confirmed = confirm("Are you sure you want to delete?");
        if (has_confirmed) {
	    var delete_url = $(".delete-entry-url").val();
	    var entry_id = $(this).attr("id").match(/(\d+)/)[1];
	    $.post(delete_url, {entry_id: entry_id}, function(data) {
	        window.location = data;
	    });
        }   
    });

    $("table#stock-items tr:odd").addClass("table-row-colour");
});
