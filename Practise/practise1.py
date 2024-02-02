# list=[1,2,3,4,5,6]
# list.add(45)
# print(list)

# lambda -limited to single expression
# a=(lambda x:"even" if x%2==0 else "odd")(2)
# print(a)

# num=267
# b=(lambda num:"even" if num%2==0 else "odd")(num)
# print(b)

# number=int(input("Enter the number:"))
# result=(lambda number:number**number)(number)
# print(result)

# Positional argument
# value=(lambda x,y,z:x+y+z)(1,2,3)
# print(value)

# named argument(keyword argument)
# value=(lambda a,b,c=5:a+b-c)(a=9,b=10)
# print(value)

# num=(lambda m,n,c:m**m+n-c)(2,3,4)
# print(num)

# varargs(*args)
# num=(lambda *args: sum(args))(1,2,3,4)
# print(num)

# num=(lambda args:sum(args))(range(1,11))
# print(num)
# n=int(input("Enter the number : "))
# result=(lambda args:sum(args))(range(1,n+1))
# print(result)

# num=sum(map(lambda *args:sum(args),(range(1,11))))
# print(num)

# variable list of keyword argument(**kwargs)
# obj=(lambda **kwargs:sum(kwargs.values()))(one=1,two=2,three=3)
# print(obj)


# Exercise 1: Calculate the multiplication and sum of two numbers
# num1=int(input("Enter the first number : "))
# num2=int(input("Enter the second number : "))
# print("The multification of twp numbers is ", num1*num2)
# print("The sum of two numbwrs is  ", num1+num2)

#Exercise2: Sum and average of first n natural numbers
# number=int(input("Enter the number : "))
# sum=0
# for num in range(1,number+1,1):
#     sum=sum+num
# print("The sum of",number,"natursl number is ",sum)
# average=sum/number
# print("The average of first",number,"natural number is ",average)

# number=[12,10,65.7,34.9,20]
# sum=0
# for num in number:
#     sum=sum+num
# average=sum/len(number)
# print("sum is",sum, "and average is",average)

# input_string = input('Enter numbers separated by space ')
# print("\n")
# # Take input numbers into list
# numbers = input_string.split()

# # convert each item to int type
# for i in range(len(numbers)):
#     # convert each item to int type
#     numbers[i] = int(numbers[i])

# # Calculating the sum and average
# print("Sum = ", sum(numbers))
# print("Average = ", sum(numbers) / len(numbers))

# matrixOne = [[6,9,11],
#     [2 ,3,8]]

# matrixTwo = [[15,18,11],
    # [26,16,19]]

# result = [[0,0,0],
#          [0,0,0]]
# for i in range(len(matrixOne)):
#     for j in range(len(matrixOne[0])):
#         result[i][j]=matrixOne[i][j]+matrixTwo[i][j]
# print("Addition of two matrix in python")
# for res in result:
#     print(res)

matrixOne = [[6,9,11],[2 ,3,8]]
# [[1,2,3],[4,5,6]]
result=[[0,0],[0,0],[0,0]]
for i in range(len(matrixOne)):
    for j in range(len(matrixOne[0])):
        result[j][i]=matrixOne[i][j]
print("Transpose matrix")
for res in result:
    print(res)
