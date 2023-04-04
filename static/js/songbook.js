/**
 * Js script for music aid songbook app
 */


/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener("DOMContentLoaded", function() {

    /**
     * Function to intercept paste events into summernote and remove all formatting and html.
     * Plain text is returned to the summernote window.
     */
    window[0].addEventListener('paste', function(event) {
        // let inputText = (event.clipboardData || window.clipboardData).getData('text');
        let inputText = (event.clipboardData || window.clipboardData).getData('text/plain');
        event.preventDefault();
        console.log("test paste event", inputText)
        console.log('in sumernote paste')
        let summernoteIframe = document.getElementById('id_lyrics_iframe')
        let innerDoc = summernoteIframe.contentDocument || summernoteIframe.contentWindow.document;
        let frameContent = innerDoc.getElementsByClassName('note-editable')
        console.log("iframe content", frameContent[0].innerHTML)
        frameContent[0].innerHTML = inputText
        frameContent[0].innerText = inputText
        console.log("modifeid content", frameContent[0].innerText)
    });
    
    // Set timeout for messages code provided by Code Institute
    if (document.getElementById('msg')) {
        setTimeout(function () {
            let messages = document.getElementById('msg');
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }, 3000);
    };
    // End of set timeout for messages code provided by Code Institute

});