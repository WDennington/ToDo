# Game Rating App

## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Trello Board](#trello-board)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Continuous Integration](#continuous-integration)
* [Development](#development)
  * [Unit Testing](#unit-testing)
  * [Front-End Design](#front-end)
  * [Integration Testing](#integration-testing)
* [Footer](#footer)

## Introduction

### Objective
The objective  for this project is as follows:
To create a CRUD application using Flask, have a working relational database,  test the application and hopefully automate the process. All of this requires clear documentation.
 

### Proposal
I have chosen to make an app that allows the user to add a game to the database, update the information about the game, add a rating to the game out of 10 and finally delete the game from the database.

An outline of how CRUD will be implemented can be seen below.

**Create**:
* Add a Game with the following attributes
  * Name
  * Description
  * Age rating (choice from a drop down box)
  * Genre

**Read**:
* See which games are in the database

**Update**:
* Alter game information in the database

**Delete**:
* Remove game from the database

## Architecture
### Risk Assessment
My initial risk assessment can be seen below
<br/><br/>
![Initial](https://i.imgur.com/2Q1wUFB.png)
<br/>
My final risk assessment can be seen below 
<br/><br/>
![Final](https://i.imgur.com/5S7ejly.png)
The full risk assessment can be found [here](https://qalearning-my.sharepoint.com/:x:/r/personal/wdennington_qa_com/Documents/Risk%20Assessment.xlsx?d=w1fdd9bdb8c6f4a5ebba7f4844972412f&csf=1&web=1&e=COMFYC).

### Trello Board
The progress of my project was documented using a Trello board.
<br/><br/>
I decided to use Trello over other kanban style boards due to not knowing how other boards work, therefore spending less time learning how to use other boards. Which allowed for more development time on the app itself.
<br/><br/>
![Initial Trello](https://i.imgur.com/y73TcmS.png)
<br/>
My initial Trello board above shows my process when I had initially began the project. <br/>
My Trello board below shows how I used it by the end, adding MoSCoW functionality and prioritising user stories.
<br/><br/>
![Final Trello](https://i.imgur.com/GDfmnyo.png)
<br/>

The full board can be found at https://trello.com/b/Ysrm49wD/games.

### Entity Relationship Diagram

Below is my entity relationship diagram
<br/>
![ERD image](https://i.imgur.com/BsIguIF.png)
<br/>
This shows how my tables were linked in my database. I use the game id from the Games table as the foreign key for the Game Ratings table. This allows multiple ratings to be associated with a single game.
<br/>
If I were to have more time and knowledge, I would have implemented another table (show below) to add users and the ability to have a user login. This would allow other people to see who thought a game was worthy of what rating. It would be linked to the Game Ratings table using the rating id as the foreign key to form a many to many relationship through the use of two one to many relationships.
<br/>
![ERD Users](https://i.imgur.com/5ypPL41.png)
<br/>

### Continuous Integration
![ci pipeline diagram](https://i.imgur.com/ULIsANn.png)
<br/>
Continuous integration is used in my project to automate builds in case of servers dropping while focusing on automatic testing. In my project Jenkins will pull code from my GitHub repository then build it. Next Jenkins will run unit testing and produce a report availible to the developer.
<br/>
#### Jenkins Script
The build script can be broken into five stages, shown below.  
<br/>

**1.** Setup variables
```
export DATABASE_URI
```
The URI is saved as secret text in Jenkins to keep it secure.
<br/>
The Secret Key is set to be a random string in the __init__.py file therefore does not need to be setup or saved to Jenkins.


**2.** Installation of the virtual environment

```
sudo apt update
sudo apt install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```
<br/>

**3.** Unit 

```
python3 -m pytest tests --cov=application --cov-report term-missing
```
<br/>



As outlined in the pipeline diagram, the testing coverage report is then available on the Jenkins console.
## Development
### Unit Testing
Unit testing is used here to check the app gives the correct response to a given input. The tests are designed to assert each function returns an expected response. These tests are run automatically after every Git push using Jenkins. Jenkins prints out whether or not the tests were successsful and also gives a coverage report noting the percentage of the application that was tested.  
<br/>

![Coverage Report](https://i.imgur.com/TarytNU.png)
<br/>

### Front-End
#### Home Page
When navigating to the page with no specified path, the user is given a list of games currently in the database, sorted by rated and unrated. They are also given a navigation bar (which is part of the layout therefore shown on all pages) Allowing the user to Add a Game, Add a Rating or to return home. (Shown below)
<br/>
![home page](https://i.imgur.com/19aWaNK.png)
<br/>

CRUD implemented on this page: Update, Delete, Read
<br/><br/>

#### Add Game Page
When navigating to the /add_game path or clicking the Add Game button shown on all pages the user is given a form to fill out which will add a new game with attributes to the database. (Shown below)

<br/>![game page](https://i.imgur.com/2OBQaXt.png)<br/>

CRUD implemented on this page: Create
<br/><br/>

#### Add Rating Page
When navigating to the /add_rating path or clicking the Add Game button shown on all pages the user is given a form to fill out which will add a new rating to a game currently in the database. (Shown below)

<br/>![rating page](https://i.imgur.com/aF5B1mN.png)<br/>


CRUD implemented on this page: Create
<br/><br/>

## Footer
### Future Improvements
* As mentioned above, a future version would add user login functionality so only the creator of a rating can remove it to stop biased ratings forming.


### Author
William Dennington

### Acknowledgements
* [Harry Volker](https://github.com/htr-volker)
* [Oliver Nichols](https://github.com/OliverNichols) 
