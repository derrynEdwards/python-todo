# TO-DO APP with Flask
Small To-Do app made with Flask.

## Requirements
- Relational Database - Supports - (MySQL, Postgres, SQLite)
- Python3
- .env file based on the `.env-sample`

## Installation

### Using the Makefile for complete installation
- Clone the repo `git clone https://github.com/derrynEdwards/python-todo.git`
- `make all` to setup the venv, install required packages and run the app.

### Using the Makefile step by step
- Clone the repo `https://github.com/derrynEdwards/python-todo.git)`
- `make setup` to setup the venv
- `make install` to install the required packages in the venv
- `make start` to run the app

### Step by Step without Makefile
- Clone the repo `git clone https://github.com/derrynEdwards/python-todo.git`
- *RECOMMENDED* Create a virtual environment `python3 -m venv ~/.todo`
- Activate the virtual environment `source ~/.todo/bin/activate`
- Install the required packages `pip install --upgrade pip` `pip install -r requirements.txt`
- Start the api `python web.py`

## Testing
The TO-DO App will be running in port `5000`. 

