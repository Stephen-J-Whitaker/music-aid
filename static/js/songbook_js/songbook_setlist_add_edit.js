/**
 * Js script for music aid songbook app setlist_add_edit page
 */


/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {

    if (document.getElementById('id_setlist_name')) {
        /**
         * Use ajax to check if input entry is unique for the user
         */
        let originalSetlistName = setlistName = $('#id_setlist_name').val()

        function validateUnique() {
            if ($('#id_setlist_name').val() != '') {
                console.log(" inNER function ")
                let setlistName = $('#id_setlist_name').val()
                let setlistNameLabel = document.querySelector('label[for="id_setlist_name"]')
                $.ajax(
                {
                    type:'GET',
                    url: '/setlist_name_validate',
                    data:{
                        setlist_name: setlistName
                    },
                    success: function(data) {
                        if (data === 'in_use') {
                            if ($('#id_setlist_name').val() === originalSetlistName) {
                                $('#id_setlist_name').css('background-color', 'white');
                                setlistNameLabel.classList.remove('setlist-name-status');
                                $('#setlist-submit-btn').show();
                            } else {
                                $('#id_setlist_name').css('background-color', 'rgb(255, 137, 137)');
                                setlistNameLabel.classList.add('setlist-name-status');
                                $('#setlist-submit-btn').hide();
                            }
                        } else {
                            $('#id_setlist_name').css('background-color', 'white');
                            setlistNameLabel.classList.remove('setlist-name-status');
                            $('#setlist-submit-btn').show();
                        }
                    }
                })
            }
        }
        
        $('#id_setlist_name').keyup('input', validateUnique);
        $('#id_setlist_name').change(validateUnique);
    }

});
