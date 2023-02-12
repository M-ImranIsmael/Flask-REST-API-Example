from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Initializing the Flask app
app = Flask(__name__)

# Configuring the SQLAlchemy database URI
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///data.db"  # Creating a database called data.db in SQLAlchemy

# Creating an instance of the SQLAlchemy class and passing the Flask app to it
db = SQLAlchemy(app)

# Defining the Drink model
class Drink(db.Model):
    # Defining columns for the Drink model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    # Defining the __repr__ method to return the name and description of the drink
    def __repr__(self):
        return f"{self.name} - {self.description}"


# Defining the root endpoint
@app.route("/")
def index():
    return "Type /drinks to see available drinks!"


# Defining the endpoint for getting all drinks
@app.route("/drinks")
def get_drinks():
    # Querying all drinks from the database
    drinks = Drink.query.all()

    # Creating an empty list to store the drinks
    output = []

    # Looping through the drinks and appending each drink's name and description to the output list
    for drink in drinks:
        drink_data = {"name": drink.name, "description": drink.description}
        output.append(drink_data)

    # Returning the drinks in the output list
    return {"drinks": output}


# Defining the endpoint for getting a specific drink by its id
@app.route("/drinks/<id>")
def get_drink(id):

    # Querying the drink from the database using its id
    drink = Drink.query.get_or_404(id)

    # Returning the name and description of the drink
    return {"name": drink.name, "description": drink.description}


# Defining the endpoint for adding a drink
@app.route("/drinks", methods=["POST"])
def add_drink():
    # Creating a Drink object with the name and description from the request body
    drink = Drink(name=request.json["name"], description=request.json["description"])

    # Adding the drink to the database session and committing the database
    db.session.add(drink)
    db.session.commit()

    # Returning the id of the drink that was added
    return {"id": drink.id}


# Defining the endpoint for deleting a drink
@app.route("/drinks/<id>", methods=["DELETE"])
def delete_drink(id):
    # Querying the drink from the database using its id
    drink = Drink.query.get(id)

    # Checking if the drink exists
    if drink is None:
        return {"error": "404"}

    # Deleting the drink from the database session
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Deleted drink"}


# With the app context, create all tables defined in the models
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
