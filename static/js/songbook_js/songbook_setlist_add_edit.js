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
        let originalSetlistName = $('#id_setlist_name').val()
        console.log('original setlist name', originalSetlistName)
    
        let setlistName = $('#id_setlist_name').val();
        let trimmedSetlistName = setlistName.trim();
        $('#id_setlist_name').val(trimmedSetlistName);
        console.log('trimmed setlist name', $('#id_setlist_name').val());

        function validateUnique() {
            if ($('#id_setlist_name').val() != '') {
                console.log(" inNER function ")
                setlistName = $('#id_setlist_name').val()
                // Replace regex for multi white space removal sourced at:
                // https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php
                trimmedSetlistName = setlistName.trimStart().replace(/  +/g, ' ');
                $('#id_setlist_name').val(trimmedSetlistName);
                setlistName = trimmedSetlistName.trimEnd();
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
                            if ($('#id_setlist_name').val().trimEnd() === originalSetlistName) {
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

        /**
         * Switch off submit event listener and submit form
         */
        function submitForm() {
            if ($('#setlist-submit-btn').is(':visible')) {
                $('form').off('submit');
                $('form').submit();
            };
        }
        
        validateUnique();
        $('#id_setlist_name').keyup('input', validateUnique);
        $('#id_setlist_name').change(validateUnique);
    
        /**
         * Trim any trailing white spaces before revalidation
         * and submit form only if save button has not been removed by
         * validation
         */
        $('form').submit(function(thisEvent) {

            console.log('in submit js')
            thisEvent.preventDefault();
            setlistName = $('#id_setlist_name').val();
            trimmedSetlistName = setlistName.trimEnd();
            // Replace regex for multi white space removal sourced at:
            // https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php
            trimmedSetlistName = trimmedSetlistName.replace(/  +/g, ' ');
            $('#id_setlist_name').val(trimmedSetlistName);
            setTimeout(validateUnique, 100);

            setTimeout(submitForm, 500);
        })

    }

});
