
[![Build Status](https://www.travis-ci.org/anyatibrian/andela-sendIT-challenge-2.svg?branch=Develop)](https://www.travis-ci.org/anyatibrian/andela-sendIT-challenge-2)[![Coverage Status](https://coveralls.io/repos/github/anyatibrian/andela-sendIT-challenge-2/badge.svg?branch=ft-update-delivery-order-status-161776751)](https://coveralls.io/github/anyatibrian/andela-sendIT-challenge-2?branch=ft-update-delivery-order-status-161776751)
[![Maintainability](https://api.codeclimate.com/v1/badges/c527fc07a94cbeb48e3f/maintainability)](https://codeclimate.com/github/anyatibrian/andela-sendIT-challenge-2/maintainability)
# sendIT
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories

## Requirements
- `Python3.6` - programming language that can be used on any modern computer operating system. 
- `Flask` - Python based web micro framework
- `Virtualenv` - Allows you to work on a specific project without worry of affecting other projects.
- `python-pip` - Package management system used to install and manage software packages,its a replacemnt of easy_install

## Functionality
- `create parcel delivery order` Enables user to create create parcel delivery order
- `Get all parcel delivery order` Enables user to view all parcel delivery orders made
- `Get single parcel order` Enables user  to get specific parcel delivery order
- `update parcel order status` Enables  user to update her parcel delivery order status 
- `create new user` Enables  users to create their own accounts
- `login user` Enables  users having accounts to login 
- `get all parcel orders according to the user id`Enables users to get all her specific parcel orders 

## To view the API on Heroku 
Copy this url paste it in a new tab
```
- https://sendit14.herokuapp.com/api/v1/parcels

```

## Installation
First clone this repository
```
$ https://github.com/anyatibrian/andela-sendIT-challenge-2/tree/Develop
$ cd andela-sendIT-challenge-2
```
Create virtual environment and install it
```
$ virtualenv venv
$ source/venv/bin/activate
```
Then install all the necessary dependencies
```
pip install -r requirements.txt
```

## Run the application
At the terminal or console type
```
python run.py
```
To run tests run this command at the console/terminal
```
pytest
```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
This is version one"v1" of the API
```
## End Points
|           End Point                      |     Functionality                                   |
|------------------------------------------|-----------------------------------------------------|
|     POST api/v1/parcels                  |creates a new parcel delivery order                  |  
|     GET  api/v1/parcels                  |get all the parcel delivery order                    |   
|     GET  api/v1/parcels/parcel_id        |get a specific parcel delivery order                 |  
|     PUT api/v1/parcels/parcel_id         |updates a specific parcel delivery order status      |
|     GET api/v1/users/user_id             |get all the parcel delivery order by a specific users|
|     POST api/v1/users                    |registers users                                      |
|     POST api/v1/users/login              |logs in in users                                     | 


## Contributors
- Anyatibrian
