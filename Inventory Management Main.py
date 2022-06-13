
#COSC1519 Introduction to Programming
#Assessment 3 Programming Project
#Student name: Dylan Adams
#Student number: s3849200
#Practical group : -



import os
import fileinput
#Main print program
def main():
    print()
    print('-----------------------------------------------------------')
    print('Welcome to JB LI BI Electronics Inventory Management System')
    print('-----------------------------------------------------------')
    print()
    print("Loading data from file: A3_s3849200_stock.txt")
    print()
    print('(1) Add New Item')
    print('(2) Remove Item')
    print('(3) Update Item')
    print('(4) Search Item')
    print('(5) View Inventory')
    print('(6) Save Data & Exit')
    user_choice = int(input("Enter choice: "))
    menu_selection(user_choice)
#Selection for menu, functions inside
def menu_selection(user_choice):
    if user_choice == 1:
        add_inventory()
    elif user_choice == 2:
        remove_inventory()
    elif user_choice == 3:
        update_inventory()
    elif user_choice == 4:
        search_inventory()
    elif user_choice == 5:
        view_inventory()
    elif user_choice == 6:
        exit("...Goodbye...")

def add_inventory():
    inventory_file = open('Stock.txt', 'a')
    print("Adding Inventory")
    print("================")
    item_description = input("Enter the name of the item: ") #Name of item
    item_quantity = input("Enter the quantity of the item: ") #Quantity of item to be added
    item_price = input("Enter the price of the item: ") #price of item added
    inventory_file.write(item_description + '\n')   #Writing data across files
    inventory_file.write(item_quantity + '\n')
    inventory_file.write(item_price + '\n')
    inventory_file.close()
    user_choice = input('Enter yes to confirm or no to go back: ') # Confirmation
    if user_choice == 'yes':
        print()
        print()
        print("Item succesfully added to inventory...")
        main()
    else:
        exit("...Goodbye...")
    
def remove_inventory():
    print("Removing Inventory")
    print("==================")
    item_description = input("Enter the item name to remove from inventory: ")

    file = fileinput.input('Stock.txt', inplace=True)

    for line in file:
         if item_description in line:
             for i in range(1):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    item_description
    user_choice = input('Enter yes to continue or no to exit: ') #Confirmation
    if user_choice == 'yes':
            main()
    else:
        exit("...Goodbye...")

def update_inventory():
    print("Updating Inventory")
    print("==================")
    item_description = input('Enter the item to update: ')
    item_quantity = int(input("How many would you like to add: "))

    with open('Stock.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('Stock.txt','r')
    file = f.read().split('\n') #Reading file / formating it
    for i, line in enumerate(file): #for loop to yield pairs
        if item_description in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (item_quantity)
                replace = b.replace(b, str(change)) #More formatting
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('Stock.txt', 'w') as f:
        for line in filedata:
            f.write(line)
                                            
                #Confirmation
    user_choice = input('Enter yes to confirm or no to go back: ')
    if user_choice == 'yes':
            main()
    else:
        exit()

#Search function
def search_inventory():
    print('Searching Inventory')
    print('===================')
    item_description = input('Enter the name of the item: ')
    
    f = open('Stock.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i+1]:
                print('Item:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantity: ', c, end='')
            for d in search[i+2:i+3]:
                print('Price: ', d, end='')
                print('----------')
        
    user_choice = input('Enter yes to continue or no to exit: ')
    if user_choice == 'yes':
            main()
    else:
        exit("...Goodbye...")
        
def view_inventory():
    inventory_file = open('Stock.txt', 'r') #Opening file
    item_description = inventory_file.readline()
    print('Current Inventory')
    print('-----------------')
    while item_description != '':
    #Reading lines
        item_description = item_description.rstrip('\n')
        item_quantity = inventory_file.readline()
        item_quantity = item_quantity.rstrip('\n')
            
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        item_description = inventory_file.readline()
    inventory_file.close()
#Confirmation
    user_choice = input('Enter yes to continue or no to exit: ')
    if user_choice == 'yes':
            main()
    else:
        exit("...Goodbye...")

main()
