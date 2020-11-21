# Project Title  : E-Commerce Management System
# Version        : 1.0 2020-2021
# Developed By   : Arsh Malik, Rian Borah
# Guide          : Mr. Mohitendra Dey
# Last Updated On: <YYYY-MM-DD>

'''
Required Libraries
'''

import csv
import math
import random

def newCustomer():

    #Prompts new customer to create login details

    with open('db/login/customer.csv','a', newline='') as cF:
        cV = csv.writer(cF)
        username = input('Username: ')
        password = input('Password: ')
        cV.writerow([username,password])

def adminLogin():
    '''
    Admin authentication by matching username and password from db/login/admin.csv

    Returns True if login successful, else it returns False

    '''
    with open('db/login/admin.csv','r') as cF:
        cV = csv.reader(cF)
        flag = 0
        username = input('admin username: ')
        password = input('admin password: ')
        for i in cV:
            if username==i[0] and password == i[1]:
                flag = 1
                break
        if flag == 1:
            return True
        else:
            return False

def customerLogin():
    '''
    Customer authentication by matching username and password from db/login/admin.csv

    Returns True if login successful, else it returns False

    '''
    with open('db/login/customer.csv','r') as cF:
        cV = csv.reader(cF)
        flag = 0
        username = input('Customer username: ')
        password = input('Customer password: ')
        for i in cV:
            if username==i[0] and password == i[1]:
                flag = 1
                break
        if flag == 1:
            return True
        else:
            return False

def addItem():
    '''
    '''
    with open('db/stock/stockItems.csv','a', newline='') as cF:
        cV = csv.writer(cF)
        code = input("Item Code: ")
        name = input("Item Name: ")
        price = input("Price: ")
        category = input(":Category: ")
        cV.writerow([code,name,price,category])

# DRIVER CODE STARTS FROM HERE

while True:
    user = input('A:Admin, C:Customer, Q:Quit ')
    if user.upper() == 'A':

        if adminLogin():
            print('Login successful. Welcome!')
            # After this admin can do stuff with stockItems.csv if entire new item added
            # update currentStock.csv if quantity of existing item added
        else:
            print('Incorrect Username or Password')

    elif user.upper() == 'C':
        status = input('Login or Sign up ? ')
        if status.upper() == 'LOGIN':

            if customerLogin():
                print('Login successful. Welcome!')
                # After this customer needs to view all items from stockItems.csv
                # The items chosen need to be added to db/shopping cart/cart.csv
                # Implement changes in currentStock.csv
            else:
                print('Incorrect Username or Password')

        elif status.upper() == 'SIGN UP':
            newCustomer()
        else:
            print('Wrong option!')
    elif user.upper()=='Q':
        break

    else:
        print('Wrong option!')

addItem()
