/**
 * Js script for music aid songbook app
 */


/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {

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
    
    // Set timeout for messages code provided by Code Institute
    if (document.getElementById('msg')) {
        setTimeout(function () {
            let messages = document.getElementById('msg');
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }, 3000);
    };
    // End of set timeout for messages code provided by Code Institute

    if (document.getElementById('id_title')) {
        /**
         * Use ajax to check if input entry is unique for the user
         */
        function validateUnique() {
            let songTitle = $('#id_title').val()
            titleLabel = document.querySelector('label[for="id_title"]')
            $.ajax(
            {
                type:'GET',
                url: '/song_title_validate',
                data:{
                    song_title: songTitle
                },
                success: function(data) {
                    if (data === 'in_use') {
                        $('#id_title').css('background-color', 'rgb(255, 137, 137)');
                        titleLabel.classList.add('title-status');
                        $('#song-add-btn').hide();
                    } else {
                        $('#id_title').css('background-color', 'white');
                        titleLabel.classList.remove('title-status');
                        $('#song-add-btn').show();
                    }
                }
            })
        }

        $('#id_title').on('input', validateUnique);
        $('#id_title').change(validateUnique);
    }

});
