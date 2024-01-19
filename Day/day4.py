# num=9
# i=1
# while i<=20:
#     print(f"{num}*{i}={num*i}")
#     i=i+1
#     if i==10:
#         continue

num=5
i=1
while num<=10:
    if i==5:
        print(f"{num} * {i}={num*i}")
        i=i+1

        continue

# num=10
# i=0
# while i<=15:
#     print(f"{num}*{i}={num*i}")
#     i=i+1
# else:
#     print("terminate the loop")



#Ask the user name and email only if user want to give them like (y/n)
# user_detail=[]
# user=input("Are you willing to fill the file(yes/no):")

# while (user=="yes"):
#     name=input("Enter the user_name:")
#     user_detail.append(name)
#     user=input("Do you want to give us email:")
# else:
#     print(user_detail)

#Let just suppose there is number 90 and get the total count  number which is divisble by 3 must be greater than 10.
# number=90
# count=0
# while number>10:
#     number=number/3
#     count=count+1
# else: 
#     print("Stop")
# print("The total number divisible by 3 is", count)

#Ask a user to enter any number between 100 and 500. We will keep asking the user to enter a correct input until he/she enters the number within a given range.
# num=int(input("Enter the number between 100 to 500 : "))
# while num>100 and num<500:
#     print("Number lies between the range from 100 to 200")
#     num=int(input("Enter the number between 100 to 500 : "))
# else:
#     print("Come out from the loop")



# n=int(input("Enter the number:"))
# while n>0:
#     if n%2==0:
#         print(n,f"is even number")

#     else:
#         print(n,f"is odd number")
#     n=n-1


# name="Shristi"
# i=0
# res=len(name)-1
# while i<=res:
#     print(name[i])
#     i=i+1

# num=[1,2,3,4,5]
# i=0
# res=len(num)-1 #string indices start from 0, and the last character 
# #of the string has an index of len(num) - 1.

# while i<=res:
#     print(num[i])
#     i=i+1


name=["Messi","Paulo","Maria","Paradise","di_paul"]
count=0
res=len(name)-1
while count<=res:
    print(name[count])
    count=count+1