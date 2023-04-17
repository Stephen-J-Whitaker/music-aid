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
     * Code inspired by the following post:
     * https://stackoverflow.com/questions/71334716
     */
    if (window[0]) {
        window[0].addEventListener('paste', function() {
            let summernoteIframe = document.getElementById('id_lyrics_iframe');
            let innerDoc = summernoteIframe.contentDocument || summernoteIframe.contentWindow.document;
            let frameContent = innerDoc.getElementsByClassName('note-editable');
            setTimeout(function() {
            let frameText = frameContent[0].innerText;
            frameContent[0].innerText = frameText;
        }, 300);
        });
    }

});