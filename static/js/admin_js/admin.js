/**
 * Js script for music aid admin page
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
            let summernoteIframe = document.getElementById('id_lyrics_iframe');
            let innerDoc = summernoteIframe.contentDocument || summernoteIframe.contentWindow.document;
            let frameContent = innerDoc.getElementsByClassName('note-editable');
            frameContent[0].innerHTML = inputText;
            frameContent[0].innerText = inputText;
        });
    }

});
