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

