$(document).ready(function() {
    $("#id_city").autocomplete({
        source: "/geography/search-city/"
    });

    $("#id_country").autocomplete({
        source: "/geography/search-country/"
    });

    /* Adds a new country */
    $("#add-country").click(function() {
        var value = prompt("Country:");
        if (value) {
            var input_data = {new_country: value};
            $("#countries-ajax-output").load("/geography/add-country-ajax/", input_data, function() {
            });

        }
    });
});
