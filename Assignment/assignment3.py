# Questions: 
# Create a function that reverses a given list.
# def reverse_list(value):
#     empty_list=[]
#     length=len(value)
#     for element in range(length-1,-1,-1):
#         empty_list.append(value[element])
#     return empty_list
# Given_list=["apple","bear","chair",111,45.5,True]
# call=reverse_list(Given_list)
# print(call)
 


# Write a function that takes a list as input and returns a new list containing only unique elements.

def unique_element(*args):
    empty_list=[]
    for item in args:
        if item not in empty_list:
            empty_list.append(item)
    return empty_list
user=[10,20,20,40,10,50,10,30]
final_list=unique_element(*user)
print(final_list)



# Implement a function that capitalizes the first letter of each word in a given string.

def first_letter(word):
    return word.capitalize()
    
letter="welcome"
Given_string=first_letter(letter)
print(Given_string)


# Write a function that uses list comprehension to generate a list of squares of the numbers from 1 to n.

n=int(input("Please enter the number:"))
def generate_square(num):
    return num**2
def generate_square_of_list_of_numbers(*args):
    # print(args)
    # for arg in args:
    #     # print(arg)
    #     print(generate_square(arg))
    return [generate_square(arg) for arg in args]
list_of_number=range(1,n+1)
value=generate_square_of_list_of_numbers(*list_of_number)
print(value)
    


# Write a function to transpose a given matrix (swap rows with columns).
# Given_matrix=[[1,2,3],[4,5,6]]
def transpose_matrix(matrix):
    new_list=[]
    for i in matrix:
        new_list2=[]
        for a in i:
            


    # new_list=[]
# for i in input:
#     new_list2=[]
#     for a in i:
#      pass

# Write a function to take the factorial number from the user
def factorial(num):
     if num==0:
         return 1
     else:
         return num*factorial(num-1)
user=int(input("Enter the number: "))
value=factorial(user)
print("The factorial number is",value)
