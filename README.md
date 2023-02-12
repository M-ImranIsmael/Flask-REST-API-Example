# Simple Flask REST API Example

This is a basic example of a REST API written in Flask. REST APIs allow client-server communication by making requests to a server and receiving responses in return.

## Build with

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## API Functionalities

The API in this example has four main functionalities:

- GET /drinks

  - This functionality returns all the drinks stored in the database as a JSON object. The "drinks" key in the JSON object contains an array of objects, each object representing a drink with its name and description.

- GET /drinks/<id>
  - This functionality returns a specific drink based on its id. If the drink is not found, it returns a 404 error.
- POST /drinks

  - This functionality allows us to add a new drink to the database by sending a JSON object with the drink's name and description as part of the request body. The API will return the id of the newly added drink.

- DELETE /drinks/<id>

  - This functionality allows us to delete a drink from the database by sending a DELETE request to the server with the id of the drink us want to delete. The API will return a "Deleted drink" message if the operation is successful, or an "error: 404" message if the drink was not found.

Technologies Used

The code is written in Python and uses the Flask framework to create a web application. The Flask-SQLAlchemy extension is used to interact with the SQLite database, and the SQLAlchemy library is used to define the model for the drinks data.

This is a simple example of how to can create a REST API using Flask, which can be used to interact with a database and perform CRUD operations.

## Acknowledgement

Thanks to Caleb, for providing a clear and concise overview to what REST APIs are and how to use them in Python!

Do subscribe to his channel 👉:
[Caleb Curry](https://www.youtube.com/watch?v=qbLc5a9jdXo)
