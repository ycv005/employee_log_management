$(document).ready(async function () {
    $(".datetimeinput").datetimepicker(
        {
            format: 'm/d/Y H:i',

        }
    );
    $(".datetimeinput").attr("autocomplete", "off");
});