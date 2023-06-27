#three types of errors:
# 1. syntax error
#       errors in the structure of the code
# 2. runtime error e.g.
#       errors that occur when program starts running; these are called
#  --------> EXCEPTIONS e.g.         
# ------------- value error
# ------------- name error
# 3. semantic error
#       errors in "meaning". The program will run but not do what I want it to. 

#the below is a walkthrough of CS50 lecture 3 on exceptions. 

#----Code section----
# try:
#     x = int(input("What's x?"))
#     print(f"x is {x}")
# except ValueError: #what will get executed in case of value error exceptions
#     print("x is not an integer")
#----end code-----

# you can omit ValueError to catch everything, bnut this is bad practice; you'll miss errors you didn't yet know about. Best to be explicit about the kind of errors you expect and then deal with unexpected errors by fixing the code. Best practice is to be explicit with error handling.

#above isn't the BEST way to handle the code - minimise what is in the try section that can actually raise an exception. One line or as minimal as possible. 
# 
# # BETTER IS: 
# ------------------
# try:
#     x = int(input("What's x?"))
# except ValueError: #what will get executed in case of value error exceptions
#     print("x is not an integer")
# else: #this is required because if there was an exception, x did not get defined, as nothing was passed to the left of the assignment in the second line of code (x= int...). So we need to recognise that if there's an exception, x is not assigned a value. So if no exception occurs, code moves to else; if exception occurs, code executes except only. The else makes the two actions MUTUALLY EXCLUSIVE.
#     print(f"x is {x}")
#--------------------

#------begin code section
# KEEP PROMPTING FOR VALID INPUT:

# while True: #loops forever because True is true!
#     try:
#         x = int(input("What's x?"))
#     except ValueError:
#         print("x is not an integer")
#     else: 
#         break
# print(f"x is {x}")

#---- end code section

#------begin code section
# alternative to put the break into the try section
# while True: 
#     try:
#         x = int(input("What's x?"))
#         break
#     except ValueError:
#         print("x is not an integer")
# print(f"x is {x}")

#---- end code section

#-----add in function:
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True: 
#         try:
#             x = int(input("What's x?"))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break #### instead of break we can shorten by returning x here instead as return breaks as well! 
#     return x

# main()
#--------------------

#REFACTORED:
def main():
    x = get_int("What's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True: 
        try:
            return int(input(prompt)) #<--- can return the value of x here as it will then break out!
        except ValueError:
            print("x is not an integer")

main()

# If we don't want to show an error message we can just do 
# except ValueError:
#     pass