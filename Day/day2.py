# num=int(input("Enter the number"))
# if (num%2==0):
#     print("The number is even")
# else:
#     print("The number is odd")


# lists=["Ram","Shyam","SIita"]
# if isinstance(lists,list):  #isinstance "check element or present in variable"
#     print("The type is list")
# elif isinstance(lists,tuple):
#     print("The type is tuple") 
# else:
#     print("I don't know")


# #append new student
# lists.append("hari") if len(lists)<=2 else print("No existing")

#take string as an input from user and get the number of vowel letter from it

namee=input("Enter the person name: ")
vowel=["a","e","i","o","u"]
vowel_count=0
non_vowel_count=0
for i in namee:
    if i in vowel:
        vowel_count=vowel_count+1
        # print("vowel is found",vowel_count)
    else:
        non_vowel_count=non_vowel_count+1
        # print("Vowel is not presented", non_vowel_count)

print("The number of vowel letter is ", vowel_count, "and non_vowel is ", non_vowel_count)




