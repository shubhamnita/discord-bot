# Discord_bot

A discord bot with google search functionality and storing individual user search history in AWS RDS Mysql DB.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6
discord.py [Python Package]
google-api-python-client [Python Package]
pymysql [Python Package]

Discord account
Google search Api account
AWS RDS mysql instance
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
1. Install Python from official python documentation.
2. Install pip if not already done.
3. Install python packages using below command:
      "pip install -r requirements.txt"
4. Create a server and bot in discord website. [Ref link :https://www.devdungeon.com/content/make-discord-bot-python]
5. Replace the bot secret token with token variable in credentials_store.py file.
6. Create a api id and key . [Ref link : http://code.google.com/apis/customsearch/v1/overview.html]
7. Replcae the google search api id and secret key with cse_id and key in credentials_store.py file. 
8. Create a AWS RDS mysql db instance and replace DB variables in credentials_store.py file .
```


## Running the application

First follow all the steps mentioned in installing part. 
Please execute the below command to run the application::
	python app.py


## Codebase Intro:

	 app.py -> This contains all the python code for discord bot.
	 database_connection.py -> This contains method to create connection to mysql instance.
	 search_actions.py -? This contains methods to google_search and get_history methods used for bot google seach functionality.
	 credential_store.py-> This contains all the API and db crdentials.
	

## Authors

* **Shubham Kumar** 


