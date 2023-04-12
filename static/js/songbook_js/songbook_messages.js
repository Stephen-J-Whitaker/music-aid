/**
 * Js script for music aid songbook app messages
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {
 
    // Set timeout for messages code provided by Code Institute
    if (document.getElementById('msg')) {
        setTimeout(function () {
            let messages = document.getElementById('msg');
            /* globals bootstrap */
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }, 3000);
    }
    // End of set timeout for messages code provided by Code Institute

});