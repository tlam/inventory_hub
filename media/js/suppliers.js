$(document).ready(function() {
    function supplier_number_ajax(selected_country) {
        if (!selected_country.length ) {
            selected_country = 0;
        }
        var input_data = {
            company_name: $("#id_company_name").val(),
            country_id: selected_country,
        };
        var supplier_number_ajax_url = $("#supplier-number-ajax-url").val();
        $.getJSON(supplier_number_ajax_url, input_data, function(data) {
            $("#id_supplier_no").val(data);
        });
    }

    $("#id_supplier_no").attr("readonly", "true");

    $("input#id_company_name").keyup(function() {
        var selected_country = $("#id_country option:selected").val();
        supplier_number_ajax(selected_country);
    });

    $("#id_country").change(function() {
        var selected_country = $(this).val();
        supplier_number_ajax(selected_country);
    });
});
