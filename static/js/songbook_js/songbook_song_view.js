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

    if (document.getElementById('lyric-container')) {
        console.log('there is a song container')
        document.getElementById('scroll-start').addEventListener('click', move);

        function move() {
            /**
             * Autoscroll of song lyrics function
             */
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
            let lyricHeight = parseInt(getComputedStyle(lyricContainer).height, 10);
            let buttonContainerHeight = parseInt(getComputedStyle(buttonContainer).height, 10);
            let contentContainerPosition = getComputedStyle(contentContainer).position;
            let contentContainerTop = getComputedStyle(contentContainer).top;
            let contentContainerZIndex = getComputedStyle(contentContainer).zIndex;
            let contentContainerHeight = getComputedStyle(contentContainer).height;
            let viewHeight = parseInt(getComputedStyle(contentContainer).height, 10);
            let moveDistance = lyricHeight - viewHeight + buttonContainerHeight;
            const speedLookup = {
                '1': 100,
                '2': 80,
                '3': 60,
                '4': 40,
                '5': 20
            }
            let x = speedLookup[scrollSpeed];
            console.log('move to me ', moveDistance);
            console.log('lyric height ', lyricHeight);
            console.log('view height ', viewHeight);

            function actionBoxMove() {
                /**
                 * Push the bottom of the lyric container up
                 * until bottom of lyrics reached
                 */
                console.log(i + 'px');
                lyricContainer.style.top = `${i}px`;
                console.log("computed ", getComputedStyle(lyricContainer).bottom);
                i--;
                moveBox();
            };

            function resetInterface() {
                /**
                 * Set the interface back to its default values
                 */
                contentContainer.style.position = contentContainerPosition;
                contentContainer.style.top = contentContainerTop;
                contentContainer.style.zIndex = contentContainerZIndex;
                // contentContainer.style.height = contentContainerHeight;
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

            function moveBox() {
                /**
                 * Call actionBoxMove at appropriate time interval
                 */
                lyricBottom = parseInt(getComputedStyle(lyricContainer).bottom, 10);
                console.log('computed bottom ', lyricBottom);
                console.log('computed height ', lyricHeight);
                console.log('computed button height ', buttonContainerHeight);
                // if (i < 10) {
                if (lyricBottom <= buttonContainerHeight) {
                    console.log(i);
                    scrollStop.addEventListener('click', stopMove);
                    const moveTimeout = setTimeout(actionBoxMove, x);
                    function stopMove() {
                        /**
                         * Stop auto scrolling because stop has been pressed
                         */
                        clearTimeout(moveTimeout);
                        scrollStop.removeEventListener('click', stopMove);
                        resetInterface();
                    };
                } else {
                    setTimeout(resetInterface, 3000);
                };
        
            };
            
            contentContainer.style.position = 'fixed'
            contentContainer.style.top = 0;
            contentContainer.style.zIndex = 1;
            contentContainer.style.height = '100%';
            backButton.style.display = 'none';
            editButton.style.display = 'none';
            buttonContainer.style.zIndex = 2;
            buttonContainer.style.position = 'fixed';
            lyricContainer.style.position = 'fixed';
            lyricContainer.style.zIndex = 0;
            lyricContainer.style.top = 0;
            scrollStop.style.display = 'flex';
            scrollStart.style.display = 'none';

            setTimeout(moveBox, 3000);
        
        }

    } else {
        console.log('there is no lyric container')
    }


});
