# **Music Aid : Songbook**
[‘Music Aid : Songbook’]( https://music-aid.herokuapp.com/) is a website for musicians and songwriters who want a more efficient way to manage their songs than the traditional method of using  a folder overflowing with printouts. 

The website is hosted on [Heroku](https://www.heroku.com/) and is implemented with the aid of the Python Django framework.

Any person who would like a digital songbook is able to register on the site and then enter their songs into the system. Their songs remain private to them and, with the exception of the system administrators, no one else who does not have their user credentials can access them. This protects their copywrite and that of others work on the system.

Once the user has songs in the system they are able to create setlists (subsets of the songs) and add their songs to their setlists. Many songs can be added to many setlists.

The system also includes an auto scroll feature so that a musician can play along with the lyrics as the lyrics automatically scroll up the screen.

-	[Link to live ‘Music Aid : songbook website]( https://music-aid.herokuapp.com/)

![Responsive mockup]( static/docs/images/readme-responsive-mockup.jpg)

## **Contents**

1 [Project Initiation](#1-project-initiation)

2 [Music Aid : Songbook development](#2-music-aid-songbook-development)

3 [Instructions](#3-instructions)

4 [Features](#4-features)

5 [Testing](#5-testing)

6 [Project Sign Off](#6-project-sign-off)

7 [Releases](#7-releases)

8 [Deployment](#8-deployment)

9 [Technologies Use](#9-technologies-used)

10 [Credits](#10-credits)

## **1. Project Initiation**

 - ## Agile

    - ### Epics, User Stories and Tasks

        An agile approach was taken to the planning and implementation of the project. Epics were identified for the project from the basic requirement for an internet based, digital songbook. The epics were then refined into user stories, their associated tasks and the acceptance criteria for the features developed to satisfy the user stories.

        As the project was planned, it was ensured that there was no functionality duplicated across features and that code could be reused wherever possible.

    - ### MoSCow

        Once the design planning had taken place, the number of story points to be allocated to each user story was estimated based on its tasks complexity and size. Potential users of the site were consulted to help ascertain each of the user stories relative importance and, using the MoSCoW technique, were given a priority of 'must have', 'should have' or 'could have'. There were no ‘won't have’ user stories.

    - ### Agile tools

        Tools in GitHub were used to manage the project development phase. The user stories were entered as issues along with their associated tasks and acceptance criteria as well as the acceptance criteria for the features developed to satisfy the user stories.

        The user stories were given labels that indicated the epic they belonged to, their MoSCoW rating and the number of Fibonacci scaled story points that they had been allocated. 

        Initially the user stories (issues) were placed on the product backlog (implemented using a milestone) and were then moved onto the project Iteration 1 milestone when it was decided that they would be worked on during that iteration. The iteration was a 3 week period. 

        During the Iteration, the user stories were managed in a GitHub project on a kanban board. In a logical order, the user stories were moved from the 'ToDo' to 'In Progress' and, once complete, to 'Done. 

    - ### User Story / Task Prioritisation

        The order that the user stories were worked on was dependent on the dependencies of each of the user stories. 

        The features and functionality of user stories moved into the ‘in progress’ column were often dependent on the completion of user stories worked on before them. These dependencies were ascertained during the project initiation/planning stage and the additional acceptance criteria required for each feature for the user story in question were appended to those defined for the user stories developed beforehand. By appending all new requirements to the bottom of the list of previous feature acceptance criteria, a full set of feature acceptance criteria was developed. 

    - ### Acceptance Tests

        From this full feature set list and those features acceptance criteria, manual testing procedures were developed that would ascertain if the acceptance criteria for the user stories, all the features and therefore the project as a whole had been satisfied. 

        When it was believed that a user story development had been completed, the test script compiled to that point was run through to ensure that both the new set of tests for the most recent user story and those defined beforehand, for previous user stories, all passed as all the previous functionality was required for the new user story and any other user story that uses the feature the tests relate to.

## **2. Music Aid : Songbook Development**
  - ### **Website Interface Development**

    - ### Interface Mockups
        
        The interface was developed to incorporate all of the features necessary to satisfy the user stories into an easy to navigate, intuitive and aesthetically pleasing design.
	
        - [Interface Mockups](docs/pdfs/readme-interface-mockups.pdf)
	
- ### **Music Aid : Songbook Style Development**
	
    The style of the interface was decided to be minimalistic to ensure that there are few distractions from the content. This is especially important to ensure that the lyrics can be read easily.

    -	### Interface Layout
    
        The layout was inspired by other web applications, especially those used for music application, to be familiar to the user. It is consistent across pages and easy to navigate. 

        -   Header and Footer
        
            There is a fixed header and footer and the navigation menu becomes a toggle button on small screens.

        -   Main Content

            The main content is in the middle of the screen and can be scrolled if the content overflows its container. There is a button bar immediately below the content (but within the main section of the webpage) which is where any controls for the content and actions that that user can take, reside.

            The exception to the standard layout described is the auto scroll feature. This expands the lyrics to full screen whilst retaining the button bar at then bottom. The button bar is used to exit the feature should the musician wish to do so.

        -   Responsiveness
    
            The interface was designed using a mobile first approach since it the app’s main purpose is to aid a musician whilst performing and musicians will tend to use a smaller device in this scenario.
            
            On larger devices the interface populates the centre section of the screen so as not to become too large to be easily read.

            The site is responsive and elements resize as necessary to fit on the screen in use and retain usability.

    -	### Typography

        A limited set of fonts were selected for the typography of the site. This helps to ensure that the site retains a consistent, coherent feel.
	
        -   Brand and Headers:

            The brand name, ‘Music Aid’ and the headers are the google font ‘Shirkhand’. The use of this font for the brand and headers helps to establish a brand identity that can become recognisable and contributes to the coherence of the site. It is bold and easy to read at all sizes required for the site.

        -   Site Text

            Google font Lato was selected as the primary font for all text on the site that isn’t the brand name or a header. A simple font, it helps to contribute to the minimalistic, coherent feel of the site. It resizes  well and is easy to read at all sizes required for the site.

    -   ### Colour Schemes

        The colour scheme of the interface was chosen to be calming shades of blue.

        - Interface

            Light in colour, the shades of blue of the interface contrast well with the text on the site ensuring good accessibility.

            The only exception to the colour scheme of the site is the favicon which is white text on a blue background. 

        - Text

            For coherence and aesthetics, the colour of the text is a deep shade of blue. The depth of the shade was in part determined by the necessity for contrast between the text and the backgrounds for accessibility.

        -   Shading

            All colours on the site are ‘flat’ except for any drop shadows used. Drop shadows are used on hovering over link text and buttons. In the case of the song list and setlist list drop shadows are present all of the time, (not just on hover), and are used to add interest and depth to the site. 

    -   ### Images and Graphics

        With the exception of the favicon, there are no images on the site which results in the site being as fast and responsive as possible ensuring maximum usability for the user whilst performing. Images are not a requirement to satisfy any of the user stories. 

        -   Favicon

            The site favicon is a cursive S that stands for songbook. It is white on a blue background to ensure readability when small and helps to build brand identity.

    -   ### Interface styling and User Feedback:

        Features style and user feedback is consistent across the site. In all cases a successful click action is indicated by the requested action taking place.

        -   Logos
        
            The logos on the site are all the same colour and have curved corners. On hovering over the logos they turn a lighter shade of the same colour and are styled with a drop shadow to indicate to the user that the logos are interactive features and are clickable.

        -   Navigation

            -   Navigation on larger screens

                The links of the navigation bar are in a row on larger screens. The are styled with a drop shadow on hovering over them to indicate to the user that they are interactive and are clickable.

            -   Navigation on mobile devices

                The navigation becomes a drop down that is displayed when a toggle button is clicked. The styles of the links in the drop down are the same as when the navigation is viewed on larger screens and they obtain a drop shadow on hovering over them.

                The toggle button is styled like all other buttons on the site, having rounded corners and being the same colour as the other buttons. The menu toggle goes a lighter shade of the same colour and acquires a drop shadow on hovering over it.

        -   Buttons

            Buttons have curved corners and are the same colour as the menu toggle. On hovering over the buttons they go a lighter shade of the same colour and acquire a drop shadow.
        
        -   Forms

            All forms on the site are styled with Django Python package Crispy Forms. 

            The form fields obtain a drop shadow on hovering over them, To indicate that they are interactive elements.

        -   Content

            The content consists of lists and song entities.

            -   Lists

                Items in content lists are styled as individual containers as each is a unique entity. 
                
                The containers are styled with a drop shadow at all times to differentiate them from the site interface. This gives then the appearance of being outwardly curved, standing out from the page which is both aesthetically pleasing and gives the site depth. 
                
                On non touch sensitive devices, hovering over any of the list items results in the item container expands signifying it it’s interactive. 
                
                In the in the case of a touch sensitive mobile device, touching the list item will result in the list item expanding indicating a successful click.
            
            -   Songs

                The title and artist of the song are displayed with the same font as the brand name, (signifying that the information is important), and are in a container that’s a slightly deeper tone of blue than the lyric container below. 

                The lighter background colour of the containers aids accessibility which is important given it’s the data on the page that needs to be most accessible especially when reading the lyrics during a performance. 

                All the text in the lyrics container is the same size and colour so that nothing could be distracting when reading the lyrics as it’s auto scrolling.

