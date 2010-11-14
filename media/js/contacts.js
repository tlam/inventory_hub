$(document).ready(function() {
    $(".add-email").live("click", function() {
        var contact_index = $(this).attr("id").match(/(\d+)/)[1];
        var contact_id = "#contact-" + contact_index;
        var last_child_id = $(contact_id  +" .emails .email:last").attr("id");
        var email_index = last_child_id.match(/(\d+)-(\d+)/)[2];
        var ajax_add_email_url = $("#ajax-add-email-url").val();
        var input_data = {
            contact_index: contact_index,
            email_index: email_index,
        };
        $.get(ajax_add_email_url, input_data, function(data) {
            $(contact_id + " .emails div.email:last").after(data);
        });
    });

    $(".remove-email").live("click", function() {
        var removed_id = $(this).attr("id");
        removed_id = removed_id.match(/(\d+)-(\d+)/);
        var ajax_remove_email_url = $("#ajax-remove-email-url").val();
        var email_id = $("#customer_email-" + removed_id + "-id").val();
        var input_data = {"email_id": email_id};
        $.get(ajax_remove_email_url, input_data, function(data) {
            $("#email_set-" + removed_id).remove();
        });
    });

    $(".add-phone").live("click", function() {
        var contact_index = $(this).attr("id").match(/(\d+)/)[1];
        var contact_id = "#contact-" + contact_index;
        var last_child_id = $(contact_id + " .phones .phone:last").attr("id");
        var phone_index = last_child_id.match(/(\d+)-(\d+)/)[2];
        var ajax_add_phone_url = $("#ajax-add-phone-url").val();
        var input_data = {
            contact_index: contact_index,
            phone_index: phone_index,
        };
        $.get(ajax_add_phone_url, input_data, function(data) {
            $(contact_id + " .phones div.phone:last").after(data);
        });
    });

    $(".remove-phone").live("click", function() {
        var removed_id = $(this).attr("id");
        removed_id = removed_id.match(/(\d+)-(\d+)/);
        var ajax_remove_phone_url = $("#ajax-remove-phone-url").val();
        var phone_id = $("#customer_phone-" + removed_id + "-id").val();
        var input_data = {"phone_id": phone_id};
        $.get(ajax_remove_phone_url, input_data, function(data) {
            $("#phone_set-" + removed_id).remove();
        });
    });

    $("#add-contact").click(function() {
        var last_child_id = $("#contacts .contact:last").attr("id");
        last_child_id = last_child_id.match(/(\d+)/)[1];
        var ajax_add_contact_url = $("#ajax-add-contact-url").val();
        var input_data = {
            "last_id": last_child_id,
        };
        $.get(ajax_add_contact_url, input_data, function(data) {
            $("#contacts div.contact:last").after(data);
        });
    });

    $(".remove-contact").live("click", function() {
        var contact_index = $(this).attr("id").match(/(\d+)/)[1];
        var contact_id = "#contact-" + contact_index;
        $(contact_id).remove();
    });
});
