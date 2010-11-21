$(document).ready(function() {
    $("input[name=check-all]").click(function() {
        $("input[name=checked-stocks]").attr("checked", this.checked);
    });
});
