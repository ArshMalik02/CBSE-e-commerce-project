# Project Title  : E-Commerce Management System
# Version        : 1.0 2020-2021
# Developed By   : Arsh Malik, Rian Borah
# Guide          : Mr. Mohitendra Dey
# Last Updated On: <YYYY-MM-DD>

'''
Required Libraries
Using camelCase

'''

import csv
import math
import random
import prettyfy

#CUSTOMER CONTROLS START HERE

def addtoCart():
    with open('db/stock/stockItems.csv','r') as cF:
        cR = csv.reader(cF)
        list_cR = list(cR)
        flag=0
        while True:
            id = input('ID of item: ')
            for i in list_cR:
                if i[0] == id:
                    flag = 1
                    quantity = input('Quantity of item you would like to purchase: ')
                    currentF = open('db/stock/currentStock.csv','r')
                    currentR = csv.reader(currentF)
                    L = list(currentR)
                    for c in L:
                        if id == c[0]:
                            if quantity > c[2]:
                                print('Not enough stock! Check back soon')
                                break
                            else:
                                qt = int(c[2])
                                custQt = int(quantity)
                                qt = qt - custQt
                                qt = str(qt)
                                c[2] = qt
                                with open('db/stock/currentStock.csv',"w",newline='') as curW:
                                    currentW = csv.writer(curW)
                                    currentW.writerows(L)
                                cart = open('db/shopping cart/cart.csv','w',newline='')
                                cartWrite = csv.writer(cart)
                                cartWrite.writerow(["ITEM CODE","ITEM NAME","CATEGORY","QUANTITY"])
                                cartWrite.writerow([id,i[1],i[3],quantity])
                                cart.close()
                                print('Item added in cart...')

                                break
            if flag == 0:
                print('Item not found\n Would you like to view all items?')
                choice = input('Y/N: ')
                if choice.upper() == 'Y':
                    viewStockitems()
                else: break
                           




#CUSTOMER CONTROLS END HERE

def viewCurrentstock():
    # Allows user to view all items in currentStock.csv
    f = open('db/stock/currentStock.csv','r')
    csv_f = csv.reader(f)
    for row in csv_f:
        print('{:<15}  {:<20}  {:<10}'.format(*row))
    print()

def adminCurrentedit():
    #Allow user to make changes to current stock of items

    with open('db/stock/currentStock.csv','r',newline='') as cF:
        cV = csv.reader(cF)
        l = list(cV)
        id = input('ID of Item: ')
        for i in l:
            if i[0] == id:
                F = open('db/stock/currentStock.csv','w',newline='')
                cW = csv.writer(F)
                newQuantity = input('Updated quantity of item: ')
                i[2] = newQuantity
                print('Current Stock of item updated')
                cW.writerows(l)
                break
        else:
            print('Item not found')

def removeStockitems():
    # Allows admin to remove item from stockItems.csv

    with open('db/stock/stockItems.csv','r+',newline='') as cF:
        cR = csv.reader(cF)
        itemId = input('ID of item to remove \n>>')
        lines = list()
        for row in cR:
            if row[0] != itemId:
                lines.append(row)
    with open('db/stock/stockItems.csv','w+',newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        print("Item deleted\n")

def viewStockitems():
    # Allows user to view all items in stockItems.csv

    f = open('db/stock/stockItems.csv','r')
    csv_f = csv.reader(f)
    for row in csv_f:
        print('{:<15}  {:<40}  {:<20} {:<25}'.format(*row))

    print()
    #print(prettyfy.pretty_file('db/stock/stockItems.csv'))


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
        elif adminEdit == 'R':
            removeStockitems()

def adminCurrentStock():
    while True:
        print('What would you like to do with current stock?')
        adminEdit = input('I:Edit Current Stock of Items \t C:View Current Stock Inventory \t Q:Quit\n>>')
        if adminEdit.upper() == 'Q':
            break
        elif adminEdit.upper() == 'I':
            adminCurrentedit()
        elif adminEdit.upper() == 'C':
            viewCurrentstock()

def addItem():
    '''
    Adds item to stockItems with details

    Example:
    >> Item Code: PEPSI150
    >> Item Name: PEPSICOLA 150ML
    >> Price($): 15
    >> Category: FOOD AND DRINK
    >> Quantity(in pcs): 100

    "PEPSI150,PEPSICOLA 150ML,15,FOOD AND DRINK" added to csv file
    '''
    with open('db/stock/stockItems.csv','a', newline='') as cF:
        F = open('db/stock/currentStock.csv','a',newline='')
        currentStock = csv.writer(F)
        cV = csv.writer(cF)
        code = input("Item Code: ")
        name = input("Item Name: ")
        price = input("Price($): ")
        category = input("Category: ")
        quantity = input("Quantity(in pcs): ")
        currentStock.writerow([code,name,quantity])
        cV.writerow([code,name,price,category])
        F.close()

def adminScreen():

    #Interface for admin to interact with stockItems and currentStock

    while True:
        print('What would you like to do?')
        adminEdit = input('I:View/Edit Stock Items \t C:View/Edit Current Stock Inventory \t Q:Log out \n>>')
        if adminEdit.upper() == 'Q':
            break
        elif adminEdit.upper() == 'I':
            adminStock()
        elif adminEdit.upper() == 'C':
            adminCurrentStock()

def customerScreen():

    #Interface for customer to interact with stockItems and currentStock

    while True:
        print('Greetings! What would you like to do?')
        custEdit = input('V:View all Items in stock \t C:Add items to Cart \t B:Check out \t Q:Log Out \n>>')
        if custEdit.upper() == 'Q':
            break
        elif custEdit.upper() == 'V':
            viewStockitems()
        elif custEdit.upper() == 'C':
            addtoCart()

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
                customerScreen()
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
