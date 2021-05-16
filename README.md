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
![Imgur](https://i.imgur.com/2Q1wUFB.png)
<br/>
The highlighted rows in the table were added at a later date after new risks became clear.  
The full risk assessment can be found [here](https://docs.google.com/spreadsheets/d/1rmqhFgW-Qwi52n_LbR-T77hh7dNrqLTI9gA4RVbdwOs/edit?usp=sharing).
