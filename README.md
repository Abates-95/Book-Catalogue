# Book-Catalogue
A Book Catalogue app with site to display, authentication routes, and all CRUD API routes ready to operate

.env evironment variables located below

|

Book-Catalogue API:
This is a RESTful API for a bookstore application built using Flask and SQLAlchemy.

|

Prerequisites:

Python 3.6 or higher

pip package manager

|

Installation:

Clone the repository: git clone https://github.com/Abates-95/Book-Catalogue.git

Change into the project directory: cd Book-Catalogue

Create a virtual environment: python3 -m venv venv

Activate the virtual environment: source venv\Scripts\activate *(I use windows)

Install the required packages: pip install -r requirements.txt

|

!!!

Configuration:

Create a .env file in the root directory of the project with the following environment variables:

FLASK_APP=app

FLASK_ENV=development

DATABASE_URI=postgresql://clsozlcm:o84KAbnHtJ10jAod-ah-8QlMmsqBw5Dm@drona.db.elephantsql.com/clsozlcm

!!!

|

Usage:

Activate the virtual environment: source venv\Scripts\activate *(I use windows)

Start the Flask development server: flask run

Use an API client such as Insomnia to send requests to the API endpoints.

|

API Endpoints:

Users

POST /users/register - Register a new user

POST /users/login - Log in an existing user and receive a token

GET /users/logout - Log out the current user

Books

!!!

availability expects boolean 'true' or 'false'

{"availability": true/false}

!!!

POST /books - Add a new book to the database

GET /books - Retrieve a list of all books in the database

GET /books/{id} - Retrieve a single book by its ID

PUT /books/{id} - Update a book by its ID

DELETE /books/{id} - Delete a book by its ID

|

Credits
This project was created by [Austin Bates].
