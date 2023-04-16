/**
 * Js script for music aid songbook app song view autoscroll
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {

    if (document.getElementById('scroll-speed').innerText !== '0' ) {
        document.getElementById('scroll-start').style.display = 'inline';
        document.getElementById('scroll-speed-label').style.display = 'inline';
        document.getElementById('scroll-speed').style.display = 'inline';
    }

    document.getElementById('scroll-start').addEventListener('click', move);
});


/**
 * Autoscroll of song lyrics function
 */
function move() {
    let i = 0;
    const lyricContainer = document.getElementById('lyric-container');
    const buttonContainer = document.getElementById('button-container');
    const contentContainer = document.getElementById('content-container');
    const backButton = document.getElementById('back');
    const editButton = document.getElementById('edit');
    const scrollStart = document.getElementById('scroll-start');
    const scrollStop = document.getElementById('scroll-stop');
    const scrollSpeed = document.getElementById('scroll-speed').innerText;
    let lyricBottom = parseInt(getComputedStyle(lyricContainer).bottom, 10);
    let buttonContainerHeight = parseInt(getComputedStyle(buttonContainer).height, 10);
    let contentContainerPosition = getComputedStyle(contentContainer).position;
    let contentContainerTop = getComputedStyle(contentContainer).top;
    let contentContainerZIndex = getComputedStyle(contentContainer).zIndex;
    let contentContainerWidth = getComputedStyle(contentContainer).Width;
    const speedLookup = {
        '1': 100,
        '2': 80,
        '3': 60,
        '4': 40,
        '5': 20
    };
    let x = speedLookup[scrollSpeed];

    /**
     * Push the bottom of the lyric container up
     * until bottom of lyrics reached
     */            
    function actionBoxMove() {
        lyricContainer.style.top = `${i}px`;
        i--;
        moveBox();
    }

    /**
     * Set the interface back to its default values
     */            
    function resetInterface() {
        contentContainer.style.position = contentContainerPosition;
        contentContainer.style.top = contentContainerTop;
        contentContainer.style.zIndex = contentContainerZIndex;
        contentContainer.style.width = contentContainerWidth;
        buttonContainer.style.zIndex = 0;
        buttonContainer.style.position = 'absolute';
        lyricContainer.style.position = 'static';
        lyricContainer.style.zIndex = 0;
        lyricContainer.style.top = '';
        backButton.style.display = 'flex';
        editButton.style.display = 'flex';
        scrollStop.style.display = 'none';
        scrollStart.style.display = 'flex';
    }

    /**
     * Call actionBoxMove at appropriate time interval
     */
    function moveBox() {
        /* globals AbortController */
        const abortSignal = new AbortController();
        lyricBottom = parseInt(getComputedStyle(lyricContainer).bottom, 10);

        if (lyricBottom <= buttonContainerHeight) {
            scrollStop.removeEventListener('click', exitAutoScroll);
            /**
             * Stop auto scrolling because stop has been pressed
             */       
            scrollStop.addEventListener('click', function() {
                clearTimeout(moveTimeout);
                abortSignal.abort();
                resetInterface();
            }, {signal : abortSignal.signal});

            const moveTimeout = setTimeout(actionBoxMove, x);
            
        }

    }
    
    contentContainer.style.position = 'fixed';
    contentContainer.style.top = 0;
    contentContainer.style.zIndex = 1;
    contentContainer.style.height = '100%';
    contentContainer.style.width = '100%';
    backButton.style.display = 'none';
    editButton.style.display = 'none';
    buttonContainer.style.zIndex = 2;
    buttonContainer.style.position = 'fixed';
    lyricContainer.style.position = 'fixed';
    lyricContainer.style.zIndex = 0;
    lyricContainer.style.top = 0;
    scrollStart.style.display = 'none';
    scrollStop.style.display = 'flex';
    const autoScrollTimeout = setTimeout(moveBox, 3000);

    scrollStop.addEventListener('click', exitAutoScroll);
    /**
     * Exit autoscroll mode if exit button is clicked
     */
    function exitAutoScroll() {
        clearTimeout(autoScrollTimeout);
        resetInterface();
    }
}