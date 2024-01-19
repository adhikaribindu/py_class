# a=12
# b="abcd"
# try:
#     print (a+b)
# except Exception:
#     print("Can not concatenate")

# a=10
# b=0
# try:
#     print(a/b)
# except (TypeError,ZeroDivisionError):
#     print("Stop flow od code")
    
# a=10
# b=0
# try:
#     print(a/b*c)
# except (TypeError,ZeroDivisionError,NameError):
#     print("Stop")
# print("Got error")

# a=10
# b=0
# try:
#     c=a/b
# except (TypeError,ZeroDivisionError,NameError):
#     print("Stop")
# else:   #Else will execute its part if there is no error in try and exception
#     print(c)
# finally:
#     print("Finally done")

# a=10
# b=0

# class InvalidInputException(Exception):
#     pass
# try:
#     c=a/b
#     raise InvalidInputException("Input is not value")
# except (TypeError,ZeroDivisionError,NameError):
#     print("Stop")
# else:   #Else will execute its part if there is no error in try and exception
#     print(c)
# finally:
#     print("Finally done")




dict_nam={"name":Ram,
          "fruit":apple,
          "animal":tiger}

