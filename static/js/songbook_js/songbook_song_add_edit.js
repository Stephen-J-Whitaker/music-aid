/**
 * Js script for music aid songbook app song_add_edit page
 */


/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {
    /**
     * Use ajax to check if input entry is unique for the user
     */
    // Actions to be taken on completion of form page load
    let originalTitle = $('#id_title').val();

    let songTitle = $('#id_title').val();
    let trimmedTitle = songTitle.trim();
    $('#id_title').val(trimmedTitle);

    let titleLabel = document.querySelector('label[for="id_title"]');
    titleLabel.innerHTML += '<div class="note">Note: leading, trailing and multiple spaces in a row are removed</div>';

    let titleLyrics = document.querySelector('label[for="id_lyrics"]');
    titleLyrics.innerHTML += '<div class="note">Note: Formatting is removed from pasted text</div>';

    let titleScrollSpeed = document.querySelector('label[for="id_scroll_speed"]');
    titleScrollSpeed.innerHTML += '<div class="note">Note: A speed of 0 means you don\'t want autoscroll for this song</div>';

    // End of actions to be taken on completion of form page load

    function validateUnique() {
        if ($('#id_title').val() != '') {
            /* globals $ */
            songTitle = $('#id_title').val();
            // Replace regex for multi white space removal sourced at:
            // https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php
            trimmedTitle = songTitle.trimStart().replace(/  +/g, ' ');
            songTitle = trimmedTitle.trimEnd();
            // Ajax code adapted from code found at this site:
            // https://www.geeksforgeeks.org/handling-ajax-request-in-django/
            $.ajax(
            {
                type:'GET',
                url: '/song_title_validate',
                data:{
                    song_title: songTitle
                },
                success: function(data) {
                    if (data === 'in_use') {
                        if ($('#id_title').val().trimStart().trimEnd().replace(/  +/g, ' ') === originalTitle) {
                            $('#id_title').css('background-color', 'white');
                            titleLabel.classList.remove('title-status');
                            $('#song-submit-btn').show();
                        } else {
                            $('#id_title').css('background-color', 'rgb(255, 137, 137)');
                            titleLabel.classList.add('title-status');
                            $('#song-submit-btn').hide();
                        }
                    } else {
                        $('#id_title').css('background-color', 'white');
                        titleLabel.classList.remove('title-status');
                        $('#song-submit-btn').show();
                    }
                }
            });
            // End of ajax code from https://www.geeksforgeeks.org/handling-ajax-request-in-django/
        }
    }

    /**
     * Switch off submit event listener and submit form
     */
    function submitForm() {
        if ($('#song-submit-btn').is(':visible')) {
            $('form').off('submit');
            $('form').submit();
        }
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

        thisEvent.preventDefault();
        songTitle = $('#id_title').val();
        trimmedTitle = songTitle.trimEnd();
        // Replace regex for multi white space removal sourced at:
        // https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php
        trimmedTitle = trimmedTitle.replace(/  +/g, ' ');
        $('#id_title').val(trimmedTitle);
        setTimeout(validateUnique, 100);

        setTimeout(submitForm, 300);
    });

    /**
     * Function to intercept paste events into summernote 
     * and remove all formatting and html.
     * Plain text is returned to the summernote window.
     * Code inspired by the following post:
     * https://stackoverflow.com/questions/71334716
     */
    window[0].addEventListener('paste', function() {
        let summernoteIframe = document.getElementById('id_lyrics_iframe');
        let innerDoc = summernoteIframe.contentDocument || summernoteIframe.contentWindow.document;
        let frameContent = innerDoc.getElementsByClassName('note-editable');
        setTimeout(function() {
        let frameText = frameContent[0].innerText;
        frameContent[0].innerText = frameText;
    }, 300)
    });
});
