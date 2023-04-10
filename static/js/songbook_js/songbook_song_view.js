/**
 * Js script for music aid songbook app song view autoscroll
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {

    if (document.getElementById('lyric-container')) {
        console.log('there is a song container')
        document.getElementById('scroll-start').addEventListener('click', move);

        function move() {
            /**
             * Autoscroll of song lyrics function
             */
            let i = 0;
            let x = 10;
            const lyricContainer = document.getElementById('lyric-container');
            const buttonContainer = document.getElementById('button-container');
            const contentContainer = document.getElementById('content-container');
            const backButton = document.getElementById('back');
            const editButton = document.getElementById('edit');
            let lyricBottom = parseInt(getComputedStyle(lyricContainer).bottom, 10);
            let lyricHeight = parseInt(getComputedStyle(lyricContainer).height, 10);
            let buttonContainerHeight = parseInt(getComputedStyle(buttonContainer).height, 10);
            let contentContainerPosition = getComputedStyle(contentContainer).position;
            let contentContainerTop = getComputedStyle(contentContainer).top;
            let contentContainerZIndex = getComputedStyle(contentContainer).zIndex;
            let contentContainerHeight = getComputedStyle(contentContainer).height;
            let viewHeight = parseInt(getComputedStyle(contentContainer).height, 10);
            let moveDistance = lyricHeight - viewHeight + buttonContainerHeight; 
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
                    document.getElementById('scroll-stop').addEventListener('click', stopMove);
                    const moveTimeout = setTimeout(actionBoxMove, x);
                    function stopMove() {
                        clearTimeout(moveTimeout);
                        document.getElementById('scroll-stop').removeEventListener('click', stopMove);

                        contentContainer.style.position = contentContainerPosition;
                        contentContainer.style.top = contentContainerTop;
                        contentContainer.style.zIndex = contentContainerZIndex;
                        contentContainer.style.height = contentContainerHeight;
                        buttonContainer.style.zIndex = 0;
                        buttonContainer.style.position = 'absolute';
                        lyricContainer.style.position = 'static';
                        lyricContainer.style.zIndex = 0;
                        lyricContainer.style.top = '';
                        backButton.style.display = 'flex';
                        editButton.style.display = 'flex';
                    };
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

            setTimeout(moveBox, 1500);
        
        }

    } else {
        console.log('there is no lyric container')
    }


});
