$(document).ready(function() {
    $("#add-warehouse").click(function() {
        var value = prompt("Warehouse:");
        if (value) {
            var input_data = {new_warehouse: value};
            $("#warehouses-ajax-output").load("/warehouses/add-ajax/", input_data, function() {
            });

        }
    });
});
