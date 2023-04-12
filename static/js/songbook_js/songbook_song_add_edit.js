/**
 * Js script for music aid songbook app song_add_edit page
 */


/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {

    /**
     * Function to intercept paste events into summernote 
     * and remove all formatting and html.
     * Plain text is returned to the summernote window.
     * Code inspired by the following post:
     * https://stackoverflow.com/questions/71334716
     */
    if (window[0]) {
        window[0].addEventListener('paste', function(event) {
            let inputText = (event.clipboardData || window.clipboardData).getData('text/plain');
            event.preventDefault();
            let summernoteIframe = document.getElementById('id_lyrics_iframe')
            let innerDoc = summernoteIframe.contentDocument || summernoteIframe.contentWindow.document;
            let frameContent = innerDoc.getElementsByClassName('note-editable');
            let frameHTML =  frameContent[0].innerHTML;
            let frameText = frameContent[0].innerText;
            frameHTML += inputText;
            frameText += inputText;
            frameContent[0].innerHTML = frameHTML;
            frameContent[0].innerText = frameText;
        });
    };

    if (document.getElementById('id_title')) {
        /**
         * Use ajax to check if input entry is unique for the user
         */

        let originalTitle = $('#id_title').val()
        console.log('original title', originalTitle)
    
        let songTitle = $('#id_title').val();
        let trimmedTitle = songTitle.trim();
        $('#id_title').val(trimmedTitle);
        console.log('trimmed title', $('#id_title').val());

        let titleLabel = document.querySelector('label[for="id_title"]')

        titleLabel.innerHTML += '<div class="note">Note: leading, trailing and multiple spaces in a row are removed</div>';

        function validateUnique() {
            console.log('in validate unique')
            if ($('#id_title').val() != '') {
                songTitle = $('#id_title').val();
                // Replace regex for multi white space removal sourced at:
                // https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php
                trimmedTitle = songTitle.trimStart().replace(/  +/g, ' ');
                // $('#id_title').val(trimmedTitle);
                songTitle = trimmedTitle.trimEnd();
                
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
                            if ($('#id_title').val().trimStart().trimEnd().replace(/  +/g, ' ') === originalTitle) {
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
            console.log('trim end ', trimmedTitle);
            // Replace regex for multi white space removal sourced at:
            // https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php
            trimmedTitle = trimmedTitle.replace(/  +/g, ' ');
            console.log('trim middle ', trimmedTitle);
            $('#id_title').val(trimmedTitle);
            setTimeout(validateUnique, 100);

            setTimeout(submitForm, 300);
        })

    }

});
