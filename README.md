# URL_Shortener_Python


This repository contains a Django-based User Authentication API with token-based authentication using Django Rest Framework and Knox.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration with validation and password hashing.
- User login with token-based authentication.
- Fetch user details using authenticated token.
- Token-based logout.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo



Sure, here's a sample README.md content for your project's Git repository. Remember to replace placeholders with actual information where necessary:

markdown
Copy code
# Django User Authentication API

This repository contains a Django-based User Authentication API with token-based authentication using Django Rest Framework and Knox.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration with validation and password hashing.
- User login with token-based authentication.
- Fetch user details using authenticated token.
- Token-based logout.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/aryats300/URL_Shortener_Python.git
   cd your-repo

   
Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate

Install project dependencies:
pip install -r requirements.txt


Set up your Django project by applying migrations:
python manage.py migrate

Run the development server
python manage.py runserver
Usage
Register a new user by making a POST request to /register/ endpoint with JSON payload containing user details.

Log in a user by making a POST request to /login/ endpoint with JSON payload containing username and password.

Fetch user details by making a GET request to /user/ endpoint with the token provided during login.

Log out a user by making a POST request to /logout/ endpoint.

Log out all user sessions by making a POST request to /logoutall/ endpoint.

API Endpoints
POST /register/: Register a new user.
POST /login/: Log in a user and receive an authentication token.
GET /user/: Fetch user details using an authentication token.
POST /logout/: Log out the current user.
POST /logoutall/: Log out all user sessions.
Contributing
Contributions are welcome! Here are a few ways you can contribute:

Report bugs or suggest improvements by creating issues.
Implement new features or fix existing issues by opening pull requests.



