# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#
# Author: Leah Methratta
# Date Created: 2022 03 01
# Date Revised: 2022 03 07
# Purpose: Model Shopping Mart

from tkinter import *
from PIL import ImageTk, Image
import datetime

root = Tk()
root.title('Insta Cart')


# DATA FRAMES
# ---------
# Fruit Frame
fruit_frame = LabelFrame(root, text = "Fruit", padx = 15, pady = 15)
fruit_frame.grid(row = 0, column = 0)

# Veg Frame
veg_frame = LabelFrame(root, text = "Vegetables", padx = 15, pady = 15)
veg_frame.grid(row = 0, column = 1)

# Meat Frame
meat_frame = LabelFrame(root, text = "Meats", padx = 15, pady = 15)
meat_frame.grid(row = 0, column = 2)

# Receipt Frame
receipt_frame = LabelFrame(root, text = "Receipt", padx = 15, pady = 15)
receipt_frame.grid(row = 6, column = 1)



# ARRAY/LIST
# ---------
# Fruits
FRUITS = [
    ("Mango", 5.99),
    ("Blueberry", 1.99),
    ("Banana", 0.99),
    ("Guava", 6.99)
    ]

# Vegies
VEGIES = [
    ("Beet Root", 2.99),
    ("Kale", 3.99),
    ("Squash", 3.50),
    ("Cauliflower", 4.99)
    ]

# Meats
MEATS = [
    ("Lamb Chop", 12.99),
    ("Pork Belly", 10.99),
    ("Wings", 4.50),
    ("Steak", 11.99)
    ]


# Initializing item, value to variable
amount = Variable()
# Setting initial to 0
amount.set(0)
# Variables to access later
x = 0
a = x
b = x
c = x
total = x
y = x
w = x

# Printing radiobuttons for every item in FRUITS
for fruit, price, in FRUITS:
    Radiobutton(fruit_frame, text = fruit, variable = amount, value = (fruit, price)).grid(row = 0 + a, column = 0, columnspan = 3, sticky = W+E)
    a += 1
    
# Printing radiobuttons for every item in VEGIES
for vegie, price, in VEGIES:
    Radiobutton(veg_frame, text = vegie, variable = amount, value = (vegie, price)).grid(row = 0 + b, column = 1, columnspan = 3, sticky = W+E)
    b += 1

# Printing radiobuttons for every item in MEATS    
for meat, price, in MEATS:
    Radiobutton(meat_frame, text = meat, variable = amount, value = (meat, price)).grid(row = 0 + c, column = 2, columnspan = 3, sticky = W+E)
    c += 1
   

# Returns the total cost after adding/removing item
def return_Total(operand, value):
    global total
    # Check whether item is being added or removed
    # Added
    if operand == "+":
        total += value
        #two decimal places
        total_val = "{:.2f}".format(total)
        my_label = Label(root, text = "Total: $" + str(total_val))
        my_label.grid(row = 4, column = 1 )
    # Removed
    elif operand == "-":
        total -= value
        total_val = "{:.2f}".format(total)
        my_label = Label(root, text = "Total: $" + str(total_val))
        my_label.grid(row = 4, column = 1 )  
    # If some other operand is entered, raise an exception
    else:
        raise Exception("incorrect operand and/or value used")
        
        

# Create a list         
foods = list()
# Updates list if items are added/removed        
def update_list(val, selected):
    item, value = selected
    global foods
    # Checking if item is added or removed
    # Added
    if val == "add":
        foods.append(selected)
    # Removed
    else: 
        # Checking if selected item is in list first
        if selected in foods:
            foods.remove(selected)
        # If item is not in list, raise an error
        else:
            raise Exception("item was not bought")


# Initializing text name as a variable            
name = StringVar()
# Setting name to an empty string
name.set(" ")
# Create a label that updates user on what item was added/removed
updates = Label(root, textvariable = name)
updates.grid(row = 5, column = 1, sticky = W+E)
  
#  Update label based on if item was added/removed etc.    
def label_update(val, selected):
    global foods
    item , value = selected
    # Check if item was added, removed, etc.
    # Added
    if val == "add":
        name.set("added 1 " + str(item) + ": " + str(value))
    # Removed
    elif val == "remove":
        # Check if item is in food list
        if selected in foods:
            name.set(("removed 1 "  + str(item) + ": " + str(value)))
            # Remove item from food list
            update_list("remove", selected)
        # If item is not in list, raise an error
        else:
            raise Exception("item was not bought")
    # Otherwise change label to be blank 
    else:
        name.set("-----------")
     
# Print receipt of items bought       
def print_receipt():
     global foods
     global y
     global w
     # Go through each item and value in list and print in receipt layout
     for item, value in foods:
         y += 1
         location = Label(receipt_frame, text = "LEAH'S INSTA CART").grid(row = 6, column = 1)
         separate = Label(receipt_frame, text = "---------").grid(row = 7, column = 1)
         item_num = Label(receipt_frame, text = str(y) + "). " + item + ": $" + str(value))
         item_num.grid(row = 8 + w, column = 1, sticky = W)
         w += 1
     # Get current time of transaction
     current_time = datetime.datetime.now()
     time_print = Label(receipt_frame, text = "Time : ").grid(row = w + 9, column = 1, sticky = W)
     time_of_transaction = Label(receipt_frame, text = str(current_time)).grid(row = w + 10, column = 1, sticky = W+E)
       
# Adding item        
def addItem(selected):
    item, value = selected
    # Update total after adding item 
    return_Total("+", value)
    # Update list after adding item
    update_list("add", selected)
    # Update label after adding item
    label_update("add", selected)
    
   
# Removing item  
def removeItem(selected):
    item, value = selected
    # Update total after removing item 
    return_Total("-", value)
    # Update label after removing item
    label_update("remove", selected)


# Completing transaction for user
def finish(selected):
    item, value = selected
    # Update label after completing transaction
    label_update("finish", selected)
    # Disable all buttons
    addButton.config(state= DISABLED)
    remButton.config(state = DISABLED)
    checkoutButton.config(state = DISABLED)
    # Print receipt 
    print_receipt()

    
# Add button 
addButton = Button(root, text = "Add to Cart", command = lambda: addItem(amount.get()))
addButton.grid(row = 3, column = 1, columnspan = 1, sticky = W+E)

# Remove button
remButton = Button(root, text = "Remove Item", command = lambda: removeItem(amount.get()))
remButton.grid(row = 3, column = 0, columnspan = 1, sticky = W+E)

# Check out button
checkoutButton = Button(root, text = "Checkout", command = lambda: finish(amount.get()))
checkoutButton.grid(row = 3, column = 2, columnspan = 2, sticky = W+E)

root.mainloop()