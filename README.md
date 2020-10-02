# :point_right: Enodo App Intallation Steps :star_struck: : Enodo Fullstack Engineering Challenge :white_check_mark:

## Requirements (Develompment Tools)

This App was devepled with the following dev tools:
- node 12.17.0
- npm 6.14.4
- Python 3.8.0
- Docker v19.03.12
- docker-compose v1.27.2 (optional if you're going to choose step:2)
- GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin19) (for dependency installation by pre_setup script)

## NOTE: The first step, Clone the repo if you have not. :innocent:

## :warning: PreSetup (Required) 
To convert Given xlsx input data file to sqlite3 db and install application dependencies, navigate to the root directory of the repo and execute the following command.
```
./pre_setup.sh
```
__Note__: you may get the following known errors because we have `db.sqlite3` file is existed in the `enodo-api` directory. Please, ignore the error. since existing `db.sqlite3` file is good to go. :innocent: 
```
ValueError: Table 'PropertyInfo' already exists.
System check identified some issues:
```
# Serve the App Locally via following ways:
## 1. With using Docker Compose

The Enodo App will be run locally on your pc soon, needs to navigate to the root directory of the repo and execute the following commands:
### Start serve the app (Spin up and Start development servers)
```
docker-compose up -d --build
```
This command starts build the docker images with the name `enodo-fullstack-challenge_web` for Back-end (Python:3.8 image for Django Rest Framework) and `enodo-fullstack-challenge_web-ui` for Front-end (node:12.2.0-alpine image for VueJs 2) based on thier Dockerfiles. And also starts development servers: `enodo-api` (Back-end APIs) and `enodo-gui` (Front-end GUI).

### Stop serve the app (Stop development servers)
```
docker-compose down -v
```
This command stops the docker containers (development servers) `enodo-api` (Back-end APIs) and `enodo-gui`. But, the docker images should be there with the name `enodo-fullstack-challenge_web` for Back-end (Python:3.8 image for Django Rest Framework) and `enodo-fullstack-challenge_web-ui` for Front-end (node:12.2.0-alpine image for VueJs 2).

NOTE: (__*For start again development servers*__), just need to execte the command:  ```docker-compose up -d``` without create/build the images.


## 2. Without using Docker Compose

1. __PreSetup__: 
To convert Given xlsx input data file to sqlite3 db and install application dependencies, navigate to the root directory of the repo and execute the following command.
```
./pre_setup.sh
```
2. __Activate virtual python env__ (.venv): 
Navigate to the root directory of the repo and execute the following command.
```
source enodo-api/.venv/bin/activate
```
3. __Start Back-end Server__: 
Open new terminal, Navigate to the root directory of the repo and execute the following commands. (:warning:.venv should be activated, if not then ref step: 2)
```
cd enodo-api
python3 manage.py runserver 9000
```
4. __Start Front-end Server__: 
Open new terminal, Navigate to the root directory of the repo and execute the following commands. (:warning:`npm install` should be executed via step: 1)
```
cd enodo-app
npm run serve -- --port 9001
```
## E2E Testing
Follow the instructions: See README.md file in `tests` directory.

## Back-end server URLs :star_struck:
The Back-end REST APIs should be available at http://localhost:9000/.
- The Admin Interface should be available at http://localhost:9000/admin/ .  
  - usr:pass -- admin:admin
- The Swagger Docs should be available at http://localhost:9000/swagger/.
- The ReDoc should be available at http://localhost:9000/redoc/.
## Font-end server URLs :star_struck:
The Enodo Application should be available at http://localhost:9001/.

## :tada: Finally, The Enodo Application should be available at http://localhost:9001/. :star_struck:



# Enodo Fullstack Engineering Challenge

Welcome to our Fullstack Engineering Challenge repository. This README will guide you on how to participate in this challenge.

Please fork this repo before you start working on the challenge. We will evaluate the code on the fork.


## Challenge


- [x] Front-end and backend to allow users to search, select, or unselect properties from the DB.

## Requirements
- [x] Build frontend with Element.js and Vue.js
- [x] Create DB from data in excel file (suggestion: Sqlite)
- [x] Create API to interact with database (suggestion: falcon, flask, express...)
- [x] Input field with [autocomplete](https://element.eleme.io/#/en-US/component/input#autocomplete), displaying the properties from the DB through the API.
  - [x] On Selection of search result, save as "Selected" to DB.
- [x] Table Showing selected properties:
  - [x] Column 1: Full Address
  - [x] Column 2: Class Description
  - [x] Column 3: Delete button
- [x] Include a delete button to unselect property from DB.
- [x] Add a test to your implementation.
- [x] Include a Readme on how to run your solution.

## Some Extra Features :star_struck:
### Front-end
- [x] :sunglasses: Increase User Experiance, Implemeted Extra feature :sassy_man: :point_right: Input field without autocomple. which is easy to edit for any user.
- [x] :sunglasses: Increase User Experiance, Implemeted Extra feature :sassy_man: :point_right:Easy route to `PropertyDetialPage` and "Select/Selected" action from there too. 
- [x] :star_struck: Increase User Attraction :sassy_man: :point_right: Used robots images as placeholders of propertyImages on each propertyCard.
- [x] :sunglasses: Increase User Experiance, Implemeted Extra feature :sassy_man: :point_right: Added Details button at Column 3: on Table Showing selected properties.
### Back-end (would be easy for front-end devs)
- [x] :star_struck: Implemeted Swagger and ReDoc endpoint
  - The Swagger Docs should be available at http://localhost:9000/swagger/.
  - The ReDoc should be available at http://localhost:9000/redoc/.
- [x] :cool: Search and Ordering filter for the property endpoint.
  - e.g.:
    - http://localhost:9000/property/?search=TAYLOR
    - http://localhost:9000/property/?search=TAYLOR&ordering=-longitude
    - http://localhost:9000/property/?ordering=-longitude
- [x] :cool: Get REST API Response in json/api format.
  - e.g:
    - http://localhost:9000/property/?ordering=-longitude&format=json
    - http://localhost:9000/property/?format=api
   
  
