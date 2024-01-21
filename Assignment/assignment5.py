# 1. Square each element in a list:
# Write a Python program that takes a list of numbers and uses a lambda function to square each element in the list. Print both the original list and the list of squared numbers.
# number=[1,2,3,4,5]
# squared_list=list(map(lambda n:n*n,number))
# print("Original lsit of number",number)
# print("Squared_list",squared_list)

# 2. Find the cube of odd numbers:
# Write a Python program that takes a list of numbers and uses a lambda function to filter out the odd numbers and then cubes each of the odd numbers. Print both the original list and the list of cubed odd numbers.
# number=[1,2,3,4,5,6,7,8,9,12]
# odd_number=list(filter(lambda x:x%2!=0, map(lambda x:x**3,number)))
# print(number)
# print("Cubes of odd_number",odd_number)


# 3. Calculate the sum of two lists:
# Write a Python program that takes two lists of numbers and uses a lambda function to calculate the sum of corresponding elements from both lists. Print both the lists and the resulting list of sums.
num=[10,5,6,7]
num2=[5,3,4,2]
list_num=list(map(lambda x,y:x+y,num,num2))
print("original list of number",num,num2)
print("Resulting list of sums",list_num)

# 4. Filter strings with a specific prefix:
# Write a Python program that takes a list of strings and uses a lambda function to filter out the strings that start with a specific prefix. Print both the original list and the filtered list.
string_list=["shristi","aakash","shrijana","rosni","shruu","pranisha","rahul","shreeza",]
filter_list=list(filter(lambda x:x.startswith('shr'),string_list))
print("Original list of string",string_list)
print("String with a speific prefix",filter_list)


# 5. Sort a list of tuples by the second element:
# Write a Python program that takes a list of tuples and uses a lambda function to sort the list based on the second element of each tuple. Print both the original list and the sorted list.
data = [(1, 5), (2, 3), (3, 1), (4, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Original list:", data)
print("Sorted list:", sorted_data)
