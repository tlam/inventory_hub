$(document).ready(function() {
    $("#id_customer_no").attr("readonly", "true");

    $(".customer-name input").keyup(function() {
        var input_data = {
            first_name: $("#id_first_name").val(),
            last_name: $("#id_last_name").val(),
        };  
        $.getJSON("/customers/customer-number-ajax/", input_data, function(data) {
            $("#id_customer_no").val(data);
        });
    });
});
