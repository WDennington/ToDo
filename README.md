# Game Rating App

## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Trello Board](#trello-board)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Test Analysis](#analysis-of-testing)
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
![Initial Trello](https://i.imgur.com/GDfmnyo.png)
<br/>

The full board can be found at https://trello.com/b/Ysrm49wD/games.
