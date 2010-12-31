$(document).ready(function() {
    $("#id_category").autocomplete({
        source: "/stocks/search-category/"
    });

    var stock_item = $(".stock-item-code").autocomplete({
        source: "/stocks/search-stock/" + $("#stock-category").val() + "/",
    });

    $("#stock-category").change(function() {
        var stock_item = $(".stock-item-code").autocomplete({
            source: "/stocks/search-stock/" + $(this).val() + "/",
        });
    });

    if (stock_item.data("autocomplete")) {
        stock_item.data("autocomplete")._renderItem = function(ul, item) {
            return $( "<li></li>" )
                .data( "item.autocomplete", item )
                .append( "<a>" + item.desc + " - <span>" + item.label + "</span></a>" )
                .appendTo( ul );
        };
    }

    $("#add-category").click(function() {
        var value = prompt("Category:");
        if (value) {
            var input_data = {new_category: value};
            $("#categories-ajax-output").load("/stocks/categories/add-ajax/", input_data, function() {
            });
        }
    });

    $("#add-colour").click(function() {
        var value = prompt("Colour:");
        if (value) {
            var input_data = {new_colour: value};
            $("#colours-ajax-output").load("/stocks/colours/add-ajax/", input_data, function() {
            });
        }
    });
});
