$(document).ready(function () {
    $('#loginform').validate({
        rules: {
            username: {
                required: true,
                minlenght: 3
            },
            password: {
                required: true,
                minlength: 3
            }
        },
        submitHandler: function (form) { // for demo
            return false; // for demo
        }
    });
});
