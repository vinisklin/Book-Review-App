# Book Review Website

Project made for the course CS50 - Web Programming with Python and Javascript

In this Web App, it's possible to search for books, leave reviews, read reviews from other users and view the average rate of the book. This last one is pulled from a broader audience, via a third-party APi by Goodreads, another book review website. Users are able to query for book details and book reviews programmatically via the website’s API.

## Technologies
* Python 3.7.3
* Flask 1.1.2
* PostgreSQL 12.3

## Setup
To run this project you need to: 
1. Install Python 3.x and pip. 
2. Clone/download this repository
3. In a terminal window, navigate into your project directory and run these commands:

```
$ pip3 install -r requirements.txt
$ export FLASK_APP=application.py
$ export DATABASE_URL = "postgres://fxpgscuslgeopu:3ac65b460a2b08a513c9cf999f9275cda15652baf1da02aa52160d45be5db7c8@ec2-54-175-117-212.compute-1.amazonaws.com:5432/de9bngomtahirr"
$ flask run
```

## Features
* Login System
* Read/Write other user's reviews
* Database hosted in Heroku Cloud Platform
* API Access

## Screenshots
![Login Page](/static/images/login-screen.jpg?raw=true "Login Screen")

![Search Page](/static/images/search-page.jpg?raw=true "Search Page")

![Book Page](/static/images/book-page.jpg?raw=true "Book Page")

## Inspiration
The development of this project was based on the content of the Harvard 'CS50 - Web Programming with Python and Javascript' course classes

## To Do:
* Add responsiveness to website
* Implement back function in review page
* Change numbers for stars in review page
* Show user's reviews after they log in
* Change route to user' username
