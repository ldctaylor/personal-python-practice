def do_something():
    pass

if __name__ == "__main__":
    do_something()

# What does if __name__ == "__main__" mean?

# A Python programme uses the condition if __name__ == '__main__' to **only run the code inside the if statement when the program is run directly by the Python interpreter**. The code inside the if statement is not executed when the file's code is imported as a module.

# __name__ is a special variable in Python 
# double underscores = "dunder"
# pronounce __name__ as "dunder name"
#the default value of __name__ is "__main__"
#if you import a module, the module's __name__ variable is assigned the name of the module
#e.g. import math ; math.__name__ = "math"