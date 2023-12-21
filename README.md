# Music Library Database

## Introduction
- This is my music library project for Makers Module 3 - Databases
- I set up this project using a starter project from Makers and used it to learn and practise the module objectives
- This project includes a music library database, containing two tables: `artists` and `albums`
- The main program `app.py` asks the user to choose whether they want to list the albums or artists, and prints data accordingly. An invalid user choice, prints an error message to the user.
- `albums_recipe.md` documents my design of the Album and AlbumRepository classes, as well as the relevant unit tests to test-drive development

## Objectives
I used this project to learn to:
- [x] Setup a Python project that connects to a database.
- [x] Test-drive Model and Repository classes to `SELECT` records from the database. 

## Setup
This project uses `python`, `pyenv` and `pipenv`. Here's how to install it:

```shell
# Install pyenv, a tool to manage different versions of Python.
# Clone the repository to your local machine
; git clone https://github.com/NatalieJClark/music-library-database.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Create the database
; createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
; open lib/database_connection.py

# Run the tests
; pytest

# Run the app
; python app.py
