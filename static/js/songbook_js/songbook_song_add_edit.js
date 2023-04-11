/**
 * Js script for music aid songbook app song_add_edit page
 */


/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {

    let originalTitle = $('#id_title').val()
    console.log('original title', originalTitle)

    let songTitle = $('#id_title').val();
    let trimmedTitle = songTitle.trim();
    $('#id_title').val(trimmedTitle);
    console.log('trimmed title', $('#id_title').val());

    /**
     * Function to intercept paste events into summernote 
     * and remove all formatting and html.
     * Plain text is returned to the summernote window.
     */
    if (window[0]) {
        window[0].addEventListener('paste', function(event) {
            let inputText = (event.clipboardData || window.clipboardData).getData('text/plain');
            event.preventDefault();
            let summernoteIframe = document.getElementById('id_lyrics_iframe')
            let innerDoc = summernoteIframe.contentDocument || summernoteIframe.contentWindow.document;
            let frameContent = innerDoc.getElementsByClassName('note-editable')
            frameContent[0].innerHTML = inputText
            frameContent[0].innerText = inputText
        });
    };

    if (document.getElementById('id_title')) {
        /**
         * Use ajax to check if input entry is unique for the user
         */

        function validateUnique() {
            console.log('in validate unique')
            if ($('#id_title').val() != '') {
                songTitle = $('#id_title').val();
                trimmedTitle = songTitle.trimStart();
                $('#id_title').val(trimmedTitle);
                songTitle = trimmedTitle;
                let titleLabel = document.querySelector('label[for="id_title"]')
                $.ajax(
                {
                    type:'GET',
                    url: '/song_title_validate',
                    data:{
                        song_title: songTitle
                    },
                    success: function(data) {
                        console.log('data', data);
                        if (data === 'in_use') {
                            if ($('#id_title').val() === originalTitle) {
                                $('#id_title').css('background-color', 'white');
                                titleLabel.classList.remove('title-status');
                                $('#song-submit-btn').show();
                                console.log('in validate unique oriinal title')
                            } else {
                                $('#id_title').css('background-color', 'rgb(255, 137, 137)');
                                titleLabel.classList.add('title-status');
                                $('#song-submit-btn').hide();
                                console.log('in validate unique in use')
                            }
                        } else {
                            $('#id_title').css('background-color', 'white');
                            titleLabel.classList.remove('title-status');
                            $('#song-submit-btn').show();
                            console.log('in validate unique available')
                        }
                    }
                })
            }
        }

        /**
         * Switch off submit event listener and submit form
         */
        function submitForm() {
            if ($('#song-submit-btn').is(':visible')) {
                $('form').off('submit');
                $('form').submit();
            };
        }
      
        validateUnique();
        $('#id_title').keyup('input', validateUnique);
        $('#id_title').change(validateUnique);

        /**
         * Trim any trailing white spaces before revalidation
         * and submit form only if save button has not been removed by
         * validation
         */
        $('form').submit(function(thisEvent) {

            console.log('in submit js')
            thisEvent.preventDefault();
            songTitle = $('#id_title').val();
            trimmedTitle = songTitle.trimEnd();
            $('#id_title').val(trimmedTitle);
            validateUnique();

            setTimeout(submitForm, 1000);
        })

    }

});
