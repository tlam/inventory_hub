$(document).ready(function() {
    $("#id_category").autocomplete({
        source: "/stocks/search-category/"
    });

    $(".stock-item-code").autocomplete({
        source: "/stocks/search-stock/"
    })
    .data("autocomplete")._renderItem = function(ul, item) {
        return $( "<li></li>" )
                .data( "item.autocomplete", item )
                .append( "<a>" + item.desc + " - <span>" + item.label + "</span></a>" )
                .appendTo( ul );
    };

    $("#add-category").click(function() {
        var value = prompt("Category:");
        if (value) {
            var input_data = {new_category: value};
            $("#categories-ajax-output").load("/stocks/categories/add-ajax/", input_data, function() {
            });

        }
    });
});
