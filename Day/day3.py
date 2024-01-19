# fruit=["apple","cherry","mango","orange"]

# for i in fruit:
#     if i=="orange":
#         print("Will break the loop")
#         continue
#         print("Will execute the block")
#     print("welcome")
#     print(i)


# [print(i) for i in fruit if i=="apple"]  #list comprehensive

# for i in range(1,10,3):
#     print(i)

#Break - Break the whole if searching or equal is matched or found
#Continue -continue the block but wiilnot execute the matched or search element
#pass-just pass  into next loop

#Find the range from 10 to20 anf if 18 is there than break and if 15 is found than continue it
    
# for i in range(10,20):
#     if i==15:
#         print("Execute the number")
#         continue
#     elif i==18:
#         print("Break the loop")
#         break

#     else:
#         pass
#     print(i)


dataset=[1,200,500,300,600,297,"918",400,"abcd",88,"99"]

for i in dataset:
    if isinstance (i,int):
        print(i)
    elif i.isdigit():
        print("Number is detected")
        continue
    else:
        print("Break the loop")
        break

    #Asks the user for the number and print the multiplication table of that specific number.
    # You have got the student marks as {1:70, 2:30, 3:90, 4:75, 5:88, 6:86, 7:76, 8:66, 9:40} get the lists of student roll who has pass the exam
    #Get the input from user and define the odd and even
        
