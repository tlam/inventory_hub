$(document).ready(function() {
    $(".errorlist").hide().fadeIn("slow");
    $(".messages").hide().fadeIn("slow");

    $(function() {
        $(".date-field").datepicker({
            dateFormat: 'yy-mm-dd'
        });
    });
});
