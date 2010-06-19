$(document).ready(function() {
    $("#id_city").autocomplete({
        source: "/geography/search-city/"
    });

    $("#id_country").autocomplete({
        source: "/geography/search-country/"
    });
});
