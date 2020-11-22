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

def removeStockitems():
    with open('db/stock/stockItems.csv','r+',newline='') as cF:
        cR = csv.reader(cF)
        itemId = input('ID of item to remove \n>>')
        #flag = 0
        for i in cR:
            if itemId == i[0]:
                flag = 1
                print('Item found...\n removing...')
                # Complete this function

def viewStockitems():
    # Allows user to view all items in stockItems.csv
    
    with open('db/stock/stockItems.csv','r') as cF:
        cV = csv.reader(cF)
        for i in cV:
            print(i)
            
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
        username = input('Admin Username: ')
        password = input('Admin Password: ')
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
def adminStock():
    while True:
        print('What would you like to do?')
        adminEdit = input('V:View Stock Items \t A:Add Stock Items \t R:Remove Stock Items \t Q:Quit \n>>')
        if adminEdit.upper() == 'Q':
            break
        elif adminEdit.upper() == 'A':
            addItem()
        elif adminEdit.upper() == 'V':
            viewStockitems()
        #elif adminEdit == 'R':
        #    adminCurrentStock()

def adminCurrentStock():
    while True:
        print('What would you like to do?')
        adminEdit = input('I:View/Edit Stock Items \t C:View/Edit Current Stock Inventory \t Q:Quit')
        if adminEdit == 'Q':
            break
        elif adminEdit == 'I':
            adminStock()
        elif adminEdit == 'C':
            adminCurrentStock()

def addItem():
    '''
    Adds item to stockItems with details

    Example:
    >> Item Code: PEPSI150
    >> Item Name: PEPSICOLA 150ML
    >> Price($): 15
    >> Category: FOOD AND DRINK

    "PEPSI150,PEPSICOLA 150ML,15,FOOD AND DRINK" added to csv file
    '''
    with open('db/stock/stockItems.csv','a', newline='') as cF:
        cV = csv.writer(cF)
        code = input("Item Code: ")
        name = input("Item Name: ")
        price = input("Price($): ")
        category = input("Category: ")
        cV.writerow([code,name,price,category])

def adminScreen():
    
    #Interface for admin to interact with stockItems and currentStock
    
    while True:
        print('What would you like to do?')
        adminEdit = input('I:View/Edit Stock Items \t C:View/Edit Current Stock Inventory \t Q:Quit \n>>')
        if adminEdit.upper() == 'Q':
            break
        elif adminEdit.upper() == 'I':
            adminStock()
        elif adminEdit.upper() == 'C':
            adminCurrentStock()

# DRIVER CODE STARTS FROM HERE
while True:
    user = input('A:Admin \t C:Customer \t Q:Quit \n>>')
    if user.upper() == 'A':

        if adminLogin():
            print('Login successful. Welcome!')
            # After this admin can do stuff with stockItems.csv if entire new item added
            # update currentStock.csv if quantity of existing item added
            adminScreen()

        else:
            print('Incorrect Username or Password\n')

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
