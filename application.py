import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Read user's inputs
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if username is already used
        if db.execute("SELECT * FROM users_table WHERE username = :username", {"username": username}).rowcount != 0:
            return render_template("registration.html", message="Username is already in use. Try another one :)")
        else:
            # Insert new user in users's table
            db.execute("INSERT INTO users_table (name, username, password) VALUES (:name, :username, :password)",
                    {"name": name, "username": username, "password": password})
            db.commit()
            return render_template("registration.html", message="Registered successfully!")
    else:
        return render_template("registration.html")


@app.route("/login", methods=["POST"])
def login():
    # Read user's inputs
    username = request.form.get("username")
    password = request.form.get("password")

    user = db.execute("SELECT * FROM users_table WHERE username = :username", {"username": username}).fetchone()
    # Check if username is in DB
    if user == None:
        return render_template("index.html", message="Invalid username")
    else:
        # Check if password is correct
        if user.password != password:
            return render_template("index.html", message="Invalid password")
        else:
            return render_template("login.html", name=user.name)
