# Write a function called calculate_area that takes two positional arguments, length and width, and returns the area of a rectangle. Test the function with different values for length and width.

def calculate_area(l,w):
    area_of_rectangle=l*w
    return area_of_rectangle
length1=int(input("Enter the length of the rectangle:" ))
width1=int(input("Enter the width of the rectangle: "))
output1=calculate_area(length1,width1)
print("The area of the rectangle is ",output1)

length2=int(input("Enter the length of the rectsngle :"))
width2=int(input("Enter the width of the rectangle :"))
output2=calculate_area(length2,width2)
print("The area of rectangle is",output2)

# Keyword Arguments:
# Create a function named print_info that takes three keyword arguments: name, age, and city. The function should print a sentence like "John is 25 years old and lives in Cityville." Test the function by passing values for each keyword argument.
def print_info(name,age,city):
    print(name,"is",age,"years old", "and lives in",city)
    return 
print_info("John",25,"cityvilla")
print_info("Zyan",33,"Canada")
print_info("Aliza",16,"USA")

# Default Arguments:
# Define a function called power that takes two arguments, base and exponent, with a default value of 2 for the exponent. The function should return the result of raising the base to the given exponent. Test the function with different values for the base and exponent.
def power(base=3,exponoent=4):
    result=base**exponoent
    return result
result=power()
print(result)



# Mix of Positional and Default Arguments:
# Write a function named greet_user that takes a positional argument name and a default argument greeting with a default value of "Hello". The function should return a greeting message using the provided name and greeting. Test the function with different names and, optionally, provide a custom greeting for some cases.
def greet_user(name="Morning",greeting="Hello"):
    print(greeting,name)
    return
greet_user(name="Afternoon")
naam,respect="Justin","Namaste"
result2=greet_user(respect)
print(result2)


# Arbitrary Number of Arguments:
# Define a function called calculate_sum that can take an arbitrary number of arguments and returns their sum. Test the function with different numbers of arguments, both positional and keyword.

def calculate_sum(*args):
    sum=0
    for num in args:
        sum=sum+num
    return sum
result=calculate_sum(1,2,3,4,5)
print(result)
