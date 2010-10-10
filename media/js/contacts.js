$(document).ready(function() {
    $("#add-email").click(function() {
        var last_child_id = $("table#emails tr:last-child").attr("id");
        last_child_id = last_child_id.match(/(\d+)/)[1];
        var ajax_add_email_url = $("#ajax-add-email-url").val();
        var input_data = {
            "last_id": last_child_id,
        };
        $.get(ajax_add_email_url, input_data, function(data) {
            $("table#emails tr:last-child").after(data);
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

    $("#add-phone").click(function() {
        var last_child_id = $("table#phones tr:last-child").attr("id");
        last_child_id = last_child_id.match(/(\d+)/)[1];
        var ajax_add_phone_url = $("#ajax-add-phone-url").val();
        var input_data = {
            "last_id": last_child_id,
        };
        $.get(ajax_add_phone_url, input_data, function(data) {
            $("table#phones tr:last-child").after(data);
        });
    });

    $(".remove-phone").live("click", function() {
        var removed_id = $(this).attr("id");
        removed_id = removed_id.match(/(\d+)/)[1];
        var ajax_remove_phone_url = $("#ajax-remove-phone-url").val();
        var phone_id = $("#customer_phone-" + removed_id + "-id").val();
        var input_data = {"phone_id": phone_id};
        $.get(ajax_remove_phone_url, input_data, function(data) {
            $("#phone_set-" + removed_id).remove();
        });
    });
});
