$(document).ready(function() {
    $("#id_category").autocomplete({
        source: "/stocks/search-category/"
    });

    $("#add-category").click(function() {
        var value = prompt("Category:");
        if (value) {
            var input_data = {new_category: value};
            $("#categories-ajax-output").load("/stocks/categories/add-ajax/", input_data, function() {
            });

        }
    });
});
