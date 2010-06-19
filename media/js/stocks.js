$(document).ready(function() {
    $("#id_category").autocomplete({
        source: "/stocks/search-category/"
    });

    $("#id_country").autocomplete({
        source: "/stocks/search-category/"
    });
});
