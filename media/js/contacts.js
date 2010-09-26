$(document).ready(function() {
    $("#add-email").click(function() {
        var data = {
            "num_emails": $("#num-emails").val(),
        };
        var ajax_email_url = $("#ajax-email-url").val();
        $("#email-output").load(ajax_email_url, data, function() {
        });
    });

    $(".remove-email").live("click", function() {
        var removed_id = $(this).attr("id");
        removed_id = removed_id.match(/(\d+)/)[1];
        $("#email_set-" + removed_id).remove();
        var num_emails = $("#num-emails").val();
        num_emails -= 1;
        $("#num-emails").val(num_emails);
/*
        var data = {
            "num_emails": $("#num-emails").val(),
            "removed_id": removed_id,
        };
        var ajax_remove_email_url = $("#ajax-remove-email-url").val();
        $("#email-output").load(ajax_remove_email_url, data, function() {
        });
*/
    });
});
