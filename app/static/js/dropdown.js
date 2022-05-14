// var checkbox = document.getElementsByClassName('.mainArtist');

// for (let index = 0; index < checkbox.length; index++) {
//     const element = checkbox[index];
//     console.log(element.checked);
// }
$(document).ready(function () {
    $('.selectpicker').selectpicker();

    $('#skills').change(function () {
        $('#hidden_skills').val($('#skills').val());
    });

    $('#multiple_select_form').on('submit', function (event) {
        event.preventDefault();
        if ($('#skills').val() != '') {
            var form_data = $(this).serialize();
            $.ajax({
                url: "/ajax_add",
                method: "POST",
                data: form_data,
                success: function (data) {
                    //console.log(data);
                    $('#hidden_skills').val('');
                    $('.selectpicker').selectpicker('val', '');
                    alert(data);
                }
            })
        }
        else {
            alert("Please select framework");
            return false;
        }
    });
});