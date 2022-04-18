# STUDENT MANAGEMENT SYSTEM BASIC CRUD APP

## Descriprion </h2>
This repository contains a detailed guide on how to develop a basic crud application gives the aility to create  anew student, edit details of existing students as well as deleting records of existing students.
We will build a small web application that demonstrates how to use SQLite with Flask to perform basic data manipulation covering CRUD: Create, Read, Update, and Delete. The web application will be a basic bstudent management application that displays students list on the index/home page. Users can create, edit, and delete individual students.

### Technologies / Frameworks used

- **Python Flask**

Flask is a lightweight Python web framework that provides useful tools and features for creating web applications in the Python Language

- **SQLite**

SQLite works well with Python because the Python standard library provides the sqlite3 module, which you can use to interact with any SQLite database without having to install anything. Using SQLite with Python also requires minimal setup compared to other database engines.

## Prerequisites
- A local Python 3 programming environment.
- An understanding of basic Flask concepts.
- An understanding of basic HTML concepts.
- A basic understanding of how to use SQLite.

## Setup
To run this project, install it locally using pip3:

```python
#clone the repo
#cd to the project folder
# initialize and activate virtual environment
$ python3 -m venv venv
#activate
$ source venv/bin/activate
# install the requirements
$ pip install -r requirements.txt
$ python3 app.py
```
**NB**: Before pushing your code to github, You should add it your virtual environment to gitignore file. Then, you should create requirements. txt file and populate it with the packages you have installed. Then, on your production server, create the virtual environment and run pip install -r requirements
- Ignore all files or folders that start with a dot .
- Ignore pycache folders

## Helpful Links
* [How To Use the sqlite3 Module in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3)
* [How To Install and Set Up a Local Programming Environment for Python 3](https://www.digitalocean.com/community/tutorial_series/how-to-install-and-set-up-a-local-programming-environment-for-python-3)
* [How to Create Your First Web Application Using Flask and Python](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3)
* [How to Use Templates in a Flask Application.](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application)
* [How To Build a Website with HTML](https://www.digitalocean.com/community/tutorial_series/how-to-build-a-website-with-html)
* [How To Install and Use SQLite on Ubuntu 20.04.](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04)
