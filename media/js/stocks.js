$(document).ready(function() {
    $("#id_category").autocomplete({
        source: "/stocks/search-category/"
    });
});
