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
            // let inputText = (event.clipboardData || window.clipboardData).getData('text/plain');
            // event.preventDefault();
            let summernoteIframe = document.getElementById('id_lyrics_iframe');
            let innerDoc = summernoteIframe.contentDocument || summernoteIframe.contentWindow.document;
            let frameContent = innerDoc.getElementsByClassName('note-editable');
            setTimeout(function() {
            // let frameHTML =  frameContent[0].innerHTML;
            let frameText = frameContent[0].innerText;
            // console.log('html', frameHTML);
            console.log('frame text', frameText);
            // frameHTML += inputText;
            // frameText += frameText.replace(/\r?\n/g, '<br>');
            // frameContent[0].innerHTML = frameText;
            frameContent[0].innerText = frameText;
        }, 300)
        });
    }

});