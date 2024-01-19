# def add(a,b):
#     return a+b
# c=add(2,3)
# d=add("abcd","96")
# e=add([1,2,3],[4,5,6])
# print(c)
# print(d)
# print(e)

# def add(a,b):
#     return a+b
# a=int(input("Enter the num:"))
# b=int(input("Enter the num: "))
# c=add(a,b)
# print(c)

# def add(n1,n2):
#     result=n1+n2
#     return result

# def multiply(n1,n2):
#     value=n1*n2
#     return value 

# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# result=add(num1,num2)
# value=multiply(num1,num2)
# print(result)
# print(value)


# def find_average_marks(marks):
#     sum_marks=sum(marks)
#     total_subject=len(marks)
#     average_marks=sum_marks/total_subject

#     return average_marks

# def find_grade(average_marks):
#     if average_marks>=80:
#         grade="A"
#     elif average_marks>=60:
#         grade="B"
#     elif average_marks>=50:
#         grade="C"
#     else:
#         grade="Fail"

#     return grade

# marks=[0,50,75,49,81]

# average_marks=find_average_marks(marks)
# grade=find_grade(average_marks)

# print(average_marks)
# print(grade)

# (**kwargs) # any number  of keywoerd argument 

# def get_grade(marks):
#     if marks>=90 and marks<=100:
#         print("A+")
#     elif marks>=80 and marks<=90:
#         print("A")
#     elif marks>=70 and marks<=80:
#         print("B+")
#     elif marks>=60 and marks<=70:
#         print("B")
#     elif marks>=50 and marks<=60:
#         print("C+")
#     elif marks>=40 and marks<=50:
#         print("C")
#     elif marks>=30 and marks<=40:
#         print("D+")
#     elif marks>=20 and marks<=30:
#         print("D")
#     else:
#         print("Fail")

# marks = {
# 1: {"math": 36, "science": 80, "english": 90},
# 2: {"math": 36, "science": 80, "english": 90},
# 3: {"math": 12, "science": 10, "english": 5},
# 4: {"math": 92, "science": 54, "english": 80},
# 5: {"math": 54, "science": 90, "english": 90},
# }
# for student_id,scores in marks.items():
#     total_marks=sum(scores.values())
#     average_marks=total_marks/len(scores)
#     get_marks=get_grade(average_marks)

# print("called")
# print(f"Student{student_id}-Average Mark:{average_marks:2f},Grade:{get_marks}")

# #args- any number of argument,mutiple argument,thaaxaina kati ota number aauxa vanerw

# def name_of(*args):
#     print(args)
#     return args 
# # if return is not called then it will return nothing as come in none in result
# c=name_of(1,2,3,"abc")
# print(c)


# def num(*args,**kwargs):
#     return args, kwargs
# n=num("a",1,2,v="apple",w="light")
# print(n)

# def num(*args,**kwargs):
#     return args,kwargs

# collection=([1,2,4],{1:"apple",2:"ball"})
# print(collection)


# def calculator(*args):
#     num=0
#     for i in args:
#         num=num+i
#     return num
# cal=calculator(1,2,3,4)
# print(cal)

# def cal(*args):
#     sum=0
#     for i in args:
#         sum=sum+i 
#     return sum
# call=cal(1,2)
# print(call)




    
    