window.onload = function () {
    $('form').on('change', 'input[name="cost"]', function(event) {
        var targ = event.target

        $.ajax({
            url: "/crm/contract/edit/",
            type: "POST",
            data: $('#signupForm').serialize(),
            success: function(data) {
                $('form').html(data.result);
            },
        });
        event.preventDefault();
    });
}

window.onload = function () {
    $('form').on('change', 'input[name="price"]', function(event) {
        var targ = event.target

        $.ajax({
            url: "/crm/invoice/edit/",
            type: "POST",
            data: $('#signupForm').serialize(),
            success: function(data) {
                $('form').html(data.result);
            },
        });
        event.preventDefault();
    });
}