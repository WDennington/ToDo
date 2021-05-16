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
The objective provided for this project is as follows:
> To create a CRUD application using Flask, have a working relational database,  test the application and hopefully automate the process. All of this requires clear documentation.
> 

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

## Development
### Unit Testing
Unit testing is used here to check the app gives the correct response to a given input. The tests are designed to assert each function returns an expected response. These tests are run automatically after every Git push using Jenkins. Jenkins prints out whether or not the tests were successsful and also gives a coverage report noting the percentage of the application that was tested.  
<br/>

![Coverage Report](https://i.imgur.com/8cRmCgu.png)
<br/>

