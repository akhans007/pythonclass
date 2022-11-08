#firstnumber=5
#secondnumber=4
#print(firstnumber ** secondnumber)

#to get users

#name=input("what is your name?")
#print(name)

#1km=1000meter
#kilometervalue=int(input("what is the kilomter value you intend to convert?"))
#print("the meter value is:", kilometervalue * 1000 )

# a customer in a store is purchasing five items.
# write a program that asks for the price of each item,
# then displays the total of the purchase
# solution
#price_of_each_item = int(input("what is the price of each item?"))
#print("the total of the purchase is : ", price_of_each_item * 5)

#import tkinter as Ehis
#mainwindow = Ehis.Tk()
#mainwindow.geometry("800x500")
#mainwindow.configure(bg="gold")


#firstLabel = Ehis.Label(text="Enter a dollar value",font=("algerian", 20))
#firstLabel.grid(row=0,column=0)

#firstentry = Ehis.Entry(font=("algerian", 20))
#firstentry.grid(row=0, column=1)

#firstbutton = Ehis.button(text="Convert Value to Naira", font =("algerian", 20) command=nifemiconverter)




#mainwindow.mainloop()


#Class Example 1
#A bank pays 10% interest per amount depoisited monthly. Write an application for
# a simple interest calculator.
#Your application should have cxean entry widget to get a customrs amount deposited and
#a button to compute the interest earned which will be displayed using a messagebox. Save
#the program as Interestcalculator.py.

#solution
import tkinter as tk
from tkinter import messagebox

mainwindow = tk.Tk()
mainwindow.geometry ("600x400")
mainwindow.configure(bg="beige")

firstlabel = tk.Label(text="Enter the amount deposited", font=("Algerian", 17))
firstlabel.grid(row=0, column=0)

firstentry = tk.Entry(font=("algerian", 20))
firstentry.grid(row=0, column=1, pady=5)
def jessecalculator():
   amountdeposited = int(firstentry.get())
   interest = amountdeposited * 0.10
   messagebox.showinfo("Interest Earned", interest)




firstbutton = tk.Button(text="Calculate Interest", font=("Algerian", 17),
                       command=jessecalculator)
firstbutton.grid(row=1, column=1)

mainwindow.mainloop()



#Class Example 2
#Create a converter that will ask for amount of days from a user.
#convert that to a year and display the value

#solution

#import tkinter as tk
#from tkinter import messagebox

#mainwindow = tk . Tk()
#mainwindow.geometry ("600x400")
#mainwindow.configure(bg="purple")

#firstlabel = tk.Label(text="Amount of days", font=("Algerian", 17))
#firstlabel.grid(row=0, column=0)

#firstentry= tk.Entry()
#firstentry.grid(row=0, column=1, pady=5)
#def Ehiscalculator():
 #   amountofdays = int(firstentry.get())
  #  value = amountofdays // 365
   # messagebox.showinfo("Value Earned", value)

#firstbutton = tk.Button(text="Calculate Value", font=("Algeria",17),
 #                       command=Ehiscalculator)
#firstbutton.grid(row=1, column=1)

#mainwindow.mainloop()



#Assignment
#Develop an application (using the input function and also the tkinter) to get
#a value from the user, convert to uppercase.

#Solution= ("what is your favourite food")

#name = input("what is your favourite food at our restaurant?")
#print(name.upper())


#Class Exercise1
#write a python to loop through this tuple (5, 6, 7), and add 10 to each number
#when printing(using a for loop)

#solution
# number = (5, 6, 7,)
# for x in number:
#     print(x+10)

#Class Exercise2
# A restaurant offers only five basic foods
# Think of five simple foods and store them in a  tuple.
# (a). Use a for loop to print each food the restaurant offers.
# (b). The restaurant changes its menu,
# replacing two of the items with different foods.
# Add a line that rewrites the tuple, and then
# use a for loop to print each of the items on the revised menu.

# #Solution
# #(a).
# menu = ("pizza", "shawarma", "small chops", "burger",)
# for snacks in menu:
#     print(snacks)
# #(b).
# listofmenu = list(menu)
# print(listofmenu)
# listofmenu[1] = "chicken and chips"
# listofmenu[3] = "fish rolls"
# print(listofmenu)
# tupleofsnacks = tuple(listofmenu)
# print(tupleofsnacks)


#forloop
#Example
#names = ["James", "Okafor", "Michael", "Desmond"]
#for eachname in names:
    #print(eachname)


    #inbuiltfunctions: print(), input(), int(), float(), tuple(), list() etc
    #tuple: () or tuple()

#whileloop
#Example1
#number = 10
#while number < 30:
    #print(number)
    #number = number + 1

#Example2
# name = input("Hello user input your username")
# while name != "Jesse":
#     name = input("Not found, use a registered name")
#
# print("ok you inputted Jesse, then welcome")

#functions is a group of code that is meant to perform
#a specific task
#Example
# def sumoftwonumbers():
#     x = 10
#     y = 100
#     print(x + y)
# sumoftwonumbers()

#Example2
# def accepttwonumbersandmultiply():
#     firstnumber = int(input("Enter a first number"))
#     secondnumber = int(input("Enter a second number"))
#     print(firstnumber * secondnumber)
#
# accepttwonumbersandmultiply()

#or can be written as

def accepttwonumbersandmultiply(firstnumber, secondnumber):
    print(firstnumber * secondnumber)

#accepttwonumbersandmultiply(20,30)
