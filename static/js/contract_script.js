window.onload = function () {
    $('form').on('change', 'input[name="cost"]', function(event) {
        var targ = event.target

        $.ajax({
            url: "/crm/contract/edit/",
            method: "GET",
            data: $('#signupForm').serialize(),
            success: function(data) {
                $('form').html(data.result);
            },
        });
        event.preventDefault();
    });
}