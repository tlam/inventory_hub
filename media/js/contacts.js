$(document).ready(function() {
    $("#add-email").click(function() {
        var last_child_id = $("table tr:last-child").attr("id");
        last_child_id = last_child_id.match(/(\d+)/)[1];
        var ajax_add_email_url = $("#ajax-add-email-url").val();
        var input_data = {
            "last_id": last_child_id,
        };
        $.get(ajax_add_email_url, input_data, function(data) {
            $("table tr:last-child").after(data);
        });
    });

    $(".remove-email").live("click", function() {
        var removed_id = $(this).attr("id");
        removed_id = removed_id.match(/(\d+)/)[1];
        var ajax_remove_email_url = $("#ajax-remove-email-url").val();
        var email_id = $("#customer_email-" + removed_id + "-id").val();
        var input_data = {"email_id": email_id};
        $.get(ajax_remove_email_url, input_data, function(data) {
            $("#email_set-" + removed_id).remove();
        });
    });
});
