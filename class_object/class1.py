# class Vehicle:
#     color="red"
#     company="creata"
    
#     def design_detail(self):
#         print(f"Car is from {self.company} company which color is {self.color}")
# a=Vehicle()
# a.design_detail()
# b=Vehicle()
# b.color="blue"
# b.design_detail()

# class Person:
#     name="Angeli"
#     age=25
#     job="student"

# a=Person()
# # print(a.name,a.age)
# a.name="Sulu"
# a.age=25
# print(a.name,a.age,a.job)


# class Person:
#     name="rita"
#     age=45
#     gender="female"

#     def info(self):
#         print(f"{self.name} is a {self.gender} and her age is {self.age}")

# a=Person()
# a.name="Gita"
# a.age=32
# a.info()

# b=Person()
# b.name="Ram"
# b.gender="Male"
# b.info()




# class People:

#     def __init__(self,age): #__repr__,__str__,magic dunder method
#         self.age=age

#     def under_16(self):
#         if self.age<16:
#             return True
#         return False

# obj1=People(age=21)
# result=obj1.under_16()
# print(result)
# obj2=People(age=15)
# res=obj2.under_16()
# print(res)

# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
        
#     def sum(self):
#         return self.num1+self.num2
#         # self.difference=difference
# a=int(input("Enter the number: "))
# b=int(input("Enter the number2:"))

# c=Calculator(a,b)
# result=c.sum()
# print(result)

# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2

#     def difference(self):
#         return self.num1-self.num2
    
# value=Calculator(10,2)
# result=value.difference()
# print(result)

# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def operation(self):
#         difference_value=self.num1-self.num2
#         product_value=self.num1*self.num2
#         return difference_value,product_value
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# result=Calculator(a,b)
# difference_value,product_value=result.operation()
# print(difference_value)
# print(product_value)

# Question 1. 
# Create a Car class with attributes such as make, model, and year.
# Implement a method in the class to display the car details.

# class Car:
#     def __init__(self,name,model,year):
#         self.name=name
#         self.model=model
#         self.year=year

#     def car_detail(self):
#         return self.name,self.model,self.year
# name=Car("suzuki","aps","2020")
# value=name.car_detail()
# print(value)

# class Student:
#   def __init__(self,name,age,grades):
#     self.name=name
#     self.age=age
#     self.grades=grades
#   def average_grade(self):
#     sum_grades=sum(self.grades)
#     total_subjects=len(self.grades)
#     average=sum_grades/total_subjects
#     return f"The average grade of {self.name} is {average}"
# display=Student("Ram",21,[22,98,10])
# result=display.average_grade()
# print(result)




class Employee:
  def __init__(self,name,position,salary):
    self.name=name 
    self.position=position
    self.salary=salary

  def give_raise(self,amount):
   if amount>0:
    self.salary+=amount
    print(f"The ${amount} has been raise to an employee. New salary is {self.salary}") 
   else:
    print("Invalid amount")

  def employee_details(self):
   print(f"Employee Name : {self.name}")
   print(f"Employee position : {self.position}")
   print(f"Employee salary : {self.salary}")

display=Employee("Ram","HR",20000)
display.give_raise(10000)
display.employee_details()
