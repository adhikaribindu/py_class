# marks=int(input("Enter the number:"))
# if marks>80 and marks <100:
#     print("A")
# elif marks>100:
#     print("Please enter the valid number")
# else:
#     print("B")

# marks=[26,56,92,90,85,10,45,30]
# pass_count=0
# fail_count=0

# for i in marks:
#     if i>90 and i<=100:
#         # print("A+")
#         pass_count=pass_count+1
#     elif i>80 and i<=90:
#         # print("A")
#         pass_count=pass_count+1
#     elif i>70 and i <=80:
#         # print("B")
#         pass_count=pass_count+1
#     elif i>60 and i<=70:
#         # print("C")
#         pass_count=pass_count+1
#     else :
#         fail_count=fail_count+1
#         # print("Fail")

# print("The number of pass student are", pass_count," and the number of fail student are",fail_count)



marks=[26,56,92,90,85,10,45,30]
pass_count=0
fail_count=0

for student in marks:
    if student>50:
        pass_count=pass_count+1
    else:
        fail_count=fail_count+1
print("The total number of pass student are", pass_count ,"and the total number of fail student are",fail_count)