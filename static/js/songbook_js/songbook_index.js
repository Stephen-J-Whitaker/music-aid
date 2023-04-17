/**
 * Js script for music aid songbook app messages
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {

    /**
     * Set styles for when toggler is clicked to override bootstrap active and focus styles
     */
    document.getElementById('navbar-toggler').addEventListener('click', function() {
        let navbarToggler = this;
        this.style.backgroundColor = 'rgb(141, 177, 207)';
        this.style.boxShadow = '0px 0px 20px 1px rgb(1, 63, 110)';
        setTimeout(function() {
            navbarToggler.style.backgroundColor = 'rgb(137, 170, 196)';
            navbarToggler.style.boxShadow = 'none';
            setTimeout(function() {
                navbarToggler.removeAttribute('style');
            }, 100);
        }, 350);
    });

    /**
     * Set styles for when mouse is over menu toggler to override bootstrap active and focus styles
     */
    document.getElementById('navbar-toggler').addEventListener('mouseover', function() {
        this.style.backgroundColor = 'rgb(141, 177, 207)';
        this.style.boxShadow = '0px 0px 20px 1px rgb(1, 63, 110)';
    });

    /**
     * Set styles for when mouse leaves menu toggler to override bootstrap active and focus styles
     */
    document.getElementById('navbar-toggler').addEventListener('mouseleave', function() {
        this.style.backgroundColor = 'rgb(137, 170, 196)';
        this.style.boxShadow = 'none';
    });

    // Set timeout for messages code provided by Code Institute
    if (document.getElementById('msg')) {
        setTimeout(function () {
            let messages = document.getElementById('msg');
            /* globals bootstrap */
            let alert = new bootstrap.Alert(messages);
            if (document.getElementById('msg')) {
                alert.close();
            }
        }, 3000);
    }
    // End of set timeout for messages code provided by Code Institute

});