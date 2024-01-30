# Car Class:
# Create a Car class with attributes such as make, model, and year.
# Implement a method in the class to display the car details.
# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year

#     def car_details(self):
#         return self.make,self.model,self.year
    
# display=Car("Creata","Corolla",2024)
# result=display.car_details()
# print(result)


# Bank Account Class:
# Design a BankAccount class with attributes like account number, account holder name, and balance.
# Include methods to deposit and withdraw money, and display the account details.

# class Bank_Account:
#     def __init__(self,account_number,account_holder_name,balance):
#         self.account_number=account_number
#         self.account_holder_name=account_holder_name
#         self.balance=balance

#     def deposit(self,amount):
#         if amount>=0:
#             self.balance=self.balance+amount
#             print(f"{amount} has been deposit in your account")
#         else:
#             print(f"Please eneter the valid amount")

#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficient amount")
#         else:
#             self.balance=self.balance-amount
#             print(f"{amount} has been withdraw from your account")
    
#     def account_details(self):
#         print(f"Account Number : {self.account_number}")
#         print(f"User name : {self.account_holder_name}")
#         print(f"Balance : {self.balance}")

# account1=Bank_Account(23827372,"Shristi",1000000)
# account1.deposit(2000)
# account1.withdraw(500)
# account1.account_details()

        

# Student Class:
# Define a Student class with attributes like name, age, and grades.
# Add a method to calculate the average grade of a student.

# class Student:
#     def __init__(self,name,age,grades):
#         self.name=name
#         self.age=age
#         self.grades=grades

#     def average_grade(self):
#         total_marks=sum(self.grades)
#         total_subject=len(self.grades)
#         average=total_marks/total_subject
#         return average
    
#     def calculate(self):
#         print(f"{self.name} whose age is {self.age} has got {self.grades} grades ")
#         print(f"average garde is {self.average_grade()}")
# result=Student("Shristi",21,[90,86,92,68])
# result.calculate()

        


# Employee Class:
# Create an Employee class with attributes for employee details such as name, position, and salary.
# Implement a method to give a raise to an employee.
# class Employee:
#     def __init__(self,name,position,salary) -> None:
#         self.name=name
#         self.position=position
#         self.salary=salary
#     def give_raise(self,amount):
#         if amount>=0:
#             self.salary+=amount
#             print(f"{self.name} has received a raise ${amount} and new salary is ${self.salary}")
#         else:
#             print("Invalid salary")
#     def employee_details(self):
#         print(f"Employee name : {self.name}")
#         print(f"Employee position : {self.position}")
#         print(f"Employee salary : {self.salary}")
# display=Employee("Shristi","Developer",20000)
# display.give_raise(20000)
# display.employee_details()
        


# Book Class:
# Develop a Book class with attributes title, author, and publication year.
# Include a method to check if the book is a bestseller based on some criteria.
# class Book:
#     def __init__(self,title,author,publication_year):
#         self.title=title
#         self.author=author
#         self.publication_year=publication_year

#     def is_bestseller(self):
#         if self.publication_year>=2020:
#             return True
#         else:
#             return False
# book1=Book("Harry Potter","Adwin",1994)
# book1.is_bestseller()


# Rectangle Class:
# Build a Rectangle class with attributes length and width.
# Implement methods to calculate the area and perimeter of the rectangle.
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def calculate_area(self):
#         print(f"The area of rectangle is {self.length} * {self.width} = {self.length *self.width}")
#     def calculate_perimeter(self):
#         perimeter=2*(self.length+self.width)
#         return perimeter
# display=Rectangle(2,6)
# display.calculate_area()
# result=display.calculate_perimeter()
# print(result)



# Bank Customer Management:
# Extend the BankAccount class to include a Customer class.
# Create a method to link a customer to their bank account.

# class BankAccount:
#     def __init__(self,account_number,balance=0):
#         self.account_number=account_number
#         self.balance=balance
        
    
# class Customer:
#     def __init__(self,id,name,contact):
#         self.id=id
#         self.name=name
#         self.contact=contact

#     def link_customer(self,bank_account):
#         self.bank_account=bank_account
#         print(f"Customer {self.name} linked to account {self.account_number}")

#     def account_info(self):
#         print(f"Account number : {self.bank_account.account_number}")
#         print(f"Customer name : {self.name}")
#         print(f"Customer ID : {self.id}")
#         print(f"Customer Contact : {self.contact}")
#         print(f"Customer Balance : {self.bank_account.balance}")
# customer1=Customer(1,"Ram",9876)
# account1=BankAccount(account_number=23,balance=1000)

# account1.link_customer(customer1)
# account1.account_info()

        
# Library Catalog:
# Design a Library class that manages a catalog of books.
# Include methods to add a book, remove a book, and display the list of available books.

# class Library:
#     def __init__(self):
#         self.catalog=[]
#     def add_book(self,book):
#         self.catalog.append(book)
#         print(f"Book '{book}' added to the library.")

#     def remove_book(self,book):
#         if book in self.catalog:
#             self.catalog.remove(book)
#             print(f"Book '{book}' has been removed from the catalog.")
#         else:
#             print(f"Book '{book}' has not found in the catalog.")
#     def book_details(self):
#         if not self.catalog:
#             print("The library is empty.")
#         else:

#             print("Book is available")
#             for book in self.catalog:
#                 print(f"-{book}")
            

# display=Library()
# display.add_book("Harry Potter")
# display.add_book("Final Destination")
# display.add_book("Sleeping beauty")
# display.book_details()

# display.remove_book("sleeping beauty")
# display.book_details()


# Shape Hierarchy:
# Create a base class called Shape with methods to calculate area and perimeter.
# Derive classes like Circle, Square, and Triangle from the base class.

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,pie,radius):
        self.pie=pie
        self.radius=radius
    def area(self):
        print(f"The area of the circle is {self.pie*self.radius**2}")
    def perimeter(self):
        print(f"The perimeter of the circle is {2*self.pie*self.radius}")

class Square(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"The area of the square is {self.length*self.breadth}")
    def perimeter(self):
        print(f"The perimeter of the square is {self.length+self.breadth}")

class Triangle(Shape):
    def __init__(self,side,base,height):
        self.side=side
        self.base=base
        self.height=height
    def area(self):
        print(f"The area of the triangle is {1/2*self.base*self.height}")
    def perimeter(self):
        print(f"The perimeter of the triangle is {2*self.side+self.base}")

pie=float(input("Enter the pie value : "))
radius=int(input("Enter the radius value : "))
output=Circle(pie,radius)
output.area()
output.perimeter()

length=int(input("Enter the length : "))
breadth=int(input("Enter the breadth :"))
output=Square(length,breadth)
output.area()
output.perimeter()

side=int(input("Enter the side of the triangle : "))
base=int(input("Enter the base of the triangle : "))
height=int(input("Enter the height of the triangle : "))
output=Triangle(side,base,height)
output.area()
output.perimeter()

# Inventory Management:
# Implement an Inventory class to keep track of product stock.
# Include methods to add stock, sell items, and display the current inventory.
# class Inventory:
#     def __init__(self):
#         self.track=[]
#     def add(self,item):
#         self.track.append(item)
#         print(f"The product {item} is added in {self.track}")
#     def sell(self,item):
#         if item in self.track:
#          self.track.remove(item)
#          print("The {item} has been sell .")
#         else:
#             print(f"The {item} is not found ")
#     def current_inventory(self):
#         if not self.track:
#             print("The inventory is empty.")
#         else:
#             print("Product is available.")
#             for item in self.track:
#                 print(f"-{item}")
# display=Inventory()
# display.add("Battery")
# display.add("Board")
# display.current_inventory()

# display.sell("Motor")
# display.current_inventory()
