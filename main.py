# Project Title  : E-Commerce Management System
# Version        : 1.0 2020-2021
# Developed By   : Arsh Malik, Rian Borah
# Guide          : Mr. Mohitendra Dey
# Last Updated On: <YYYY-MM-DD>

'''
Required Libraries
'''
import mysql.connector
#install using python "-m pip install mysql-connector-python"

import csv
import math
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

users = {"rian": "ilikecats", "arsh": "comeoncity"}
#store users and password in sql instead?

def createUser():
    '''
    Prompts user to create Admin or Service ID with password
    Added to users dict if not already existing

    Example:
    >>> Enter new username: sudo
    >>> Enter password: asdfghjkl

    Adds {"sudo":"asdfghjkl"} to users dict
    '''

    username = input("Enter new username: ")
    if username not in users:
        password = input("Enter password: ")

        users[username] = password

    else:
        print("User already exists")

def login():
    '''

    '''
