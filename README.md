# **Music Aid : Songbook**
[‘Music Aid : Songbook’]( https://music-aid.herokuapp.com/) is a website The website, (hosted on [Heroku](https://www.heroku.com/) and implemented with the aid of the Python Django framework), for musicians and songwriters who want a more efficient way to manage their songs than the traditional method of using a folder overflowing with printouts.

Over time songbooks become full and unwieldy. Gathering songs together for a particular gig can be time consuming and accessing a desired song at a performance, especially quickly can be a challenge. This is where Music Aid : Songbook comes in. Music Aid : Songbook is a digital repository for all the songs belonging to a musician or songwriter.

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

-   ### Software Structure

    The Music Aid : Songbook internet application is implemented using the Python Django framework.

    Within the standard Django framework, this project is called ‘music aid’ and the application is called ‘songbook’.

    -   Django framework:

        Many files are installed when Django is installed. Some of these files require customisation in order that the code will run correctly for the application being developed. 

        A number of the application features are implemented with the aid of 3rd party Django packages.

        -   Django Packages / Software dependencies:

            A number of 3rd part Django packages were dependencies of project features.

            Installed Django packages: 
            
            |Package|Function|
            |-------|--------|
            |gunicorn|The webserver for Django|
            |dj database url|Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application|
            |psycogpg2|A PostgreSQL database adapter for the Python programming language|
            |dj3 cloudinary storage|Facilitates connection to a cloud based storage repository for static files|
            |Django allauth|Integrated set of Django applications addressing authentication, registration, account management|
            |Django summernote| A WYSIWYG (What You See Is What You Get) editor be used for lyric form field data entry|
            |Django crispy forms|Automatic formatting of forms for aesthetics and consistency of style|

        -   Music Aid project folder:

            The Music Aid project folder contains project wide code and configurations. Only some of the files within this folder require customisation and which ones depends on the specific project and its applications.

        -   Below are the files that were customised.
      
            |File|Function|
            |-------|--------|
            |Settings.py|Settings.py contains configurations such as debug mode, installed apps, widget, database and cloud storage configuration. The majority of setting.py is created automatically when a new Django project is created|
            |urls.py|urls.py required customisation to make use of the project songbook apps url paths. Urls.py also required customisation to the use the paths made available by the allauth and summernote 3rd party packages|

        -   Songbook Application Folder

            The songbook application folder contains all python files that are specific to the features provided by the songbook application. The songbook application provides create, read, update and delete (CRUD) functionality for songs and setlists on a per registered user basis (registration is implemented using the 3rd party allauth package). The following required creation and/or customisation:

            |File|Function|
            |-------|-------|
            |admin.py|Registration of custom models and customisation of the view of these models in the Django admin panel|
            |forms.py|Custom form classes used by the applications views to create forms within rendered templates|
            |models.py|Custom model classes that describe the database tables required, the fields within those tables and these tables and fields relationships with other tables and fields within the database as a whole. The data in these classes is used by Django to build the complete database schema required for the application|
            |urls.py|Contains definitions for all the url paths require by the application|
            |views.py|Custom classes that perform functions as required, render templates with the required data and return an http response in response to a url being requested by a site user or the system|

        -   Static Folder

            The static folder is hosted on cloud storage after deployment. It holds any static files for the application. In the songbook application the static folder contains the following folders and files:

            |Folder/File|Contents|
            |-------|-------|
            |css folder|Css styles sheets used by the site|
            |js|Javascript files and libraries used by the site|
            |favicon.ico|The sites favicon|

        -   Templates folder

            The templates folder contains custom templates used to implement the application and templates that can be customised.

        -   Procfile

            Contains a command to run the gunicorn webserver to serve the application. The command is run when the application is started.

        -   Requirements.txt

            A list of dependencies that require installation for the project to run correctly.

        -   Env.py

            Env.py contains all the environment variables for the software. It contains the data that must never be exposed in the public domain and so is never committed to a code repository.
            
            The Django ‘secret key’, the application database URL and the Cloudinary cloud storage URL are in the env.py file for use during the development phase of the project prior to deployment. At deployment, these environment variables are set within the environment on which they are deployed and are still kept out of the public domain after deployment.

    -   Database

        The database for the product is implemented using the PostgresSQL relational database management system (RDBMS).

        -   Database Data Models

            Some tables in the database are created as standard for all Django installations and some in response to the installation of some 3rd part packages. With the exception of the User table, (included with the definitions below due to its fields exposure on the front end in order to implement an authentication system), these tables are excluded from the ERD because they are implemented as standard as a result of the Django or a package installation and are not designed or modified by the Music Aid :songbook developer. 

            In response to the migration of custom models Django automatically creates various helper tables  to facilitate the relationships between the models. These helper link tables for the many to many relationships are also not included in the entity relationship diagram for the database as they were not designed or modified by the Music Aid : songbook developer. 

            The entire product database  schema can be recreated from the documented custom models and installation of Django and the documented 3rd party packages when the manage.py makemigrations and migrate commands are run.

            -   User model (A standard Django model)

                This is the default Django ‘user’ model. The fields shown below are fields installed automatically with Django and their use is handled automatically by the allauth package when the site is used by a user and Django admin should an administrator be using the admin panel for user administration.

                The user table is documented here due to some of it fields being exposed for direct data input in forms on the front end during user authentication.
            
            -   Song Model

                The song model holds data relating to any given users songs. 

                A song has a one to one foreign key relationship with the user who created it in the system. If that user is deleted, the users songs are deleted.

            -   Setlist model

                The setlist model holds data relating to any given users setlists. 

                A setlist has a one to one foreign key relationship with the user who created it in the system. If that user is deleted, the users songs are deleted.

                A users setlist has a many to many relationship with the users songs. Many songs can be linked to many setlists.

