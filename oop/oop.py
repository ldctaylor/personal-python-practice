###OBJECT ORIENTED PROGRAMMING

# In Python, pretty much everything is an object
# Objects have STATE and METHODS

# First we define the 
# ---> CONCEPT of a type of object (aka CLASS)
# then we create an 
# ---> an INSTANCE (individual object of that type)

#Define CLASS ATTRIBUTES
#Every object created from this class will have  these attributes/share these pieces of state.
class UnfinishedProject():
    type = "Unfinished Craft Project"
    status = "WIP"

scarf = UnfinishedProject()
print(scarf)

#Use .attribute to access the attributes of an object. 
print(f"The scarf project has a status of {scarf.status}")

# A METHOD is really just a FUNCTION THAT BELONGS TO AN OBJECT. We can define methods within the class code block.

class UnfinishedProject():
    type = "Unfinished Craft Project"
    status = "WIP"

    def speak(self):
        return "Please finish me!"

scarf = UnfinishedProject()
print(f"It says,{scarf.speak()}")

###USE OF (SELF) AS ARGUMENT WHEN DEFINING METHOD###
# It's not the "concept" of the unfinished project saying finish me; it's the instance of the unfinished project
# When python runs the speak method it wants to know which project is speaking
# When we run an instance method, Python automatically passes the instance itself through as the first argument. It does this without needing to be told. 
#So self above refers to the scarf.
#print(self) results in something like :
# ---> <_main_.ObjectName object at 0dmf3fh>

#### When you call an instance method, the instance itself is automatically passed to the method as the first argument ####

class KnittingProject():
    type = "Knitting Project"
    status = "Not Yet Started"

    def whoami(self):
        print(self)
        print("I'm a knitting project!")
    
hat = KnittingProject()
hat.whoami()

## INITIALISING
# Initialising is the act of creating an instance of a class. We have been initialising the scarf with the line scarf = UnfinishedProject()
# How can we tell one unfinishedproject from another when it is created? We need to be able to give it unique distinguishing features when we create it, by customising the __init__ method of the UnfinishedProject class.

# __init__ method is built into every class automatically. Gets called when we create an instance of that class. 

class UnfinishedProject():
    type = "Unfinished Craft Project"
    status = "WIP"

    def __init__(self,start_date,craft_category):
        # these are INSTANCE attributes
        self.startdate = start_date
        self.crafttype = craft_category

HPscarf = UnfinishedProject("Jan 2019","knitting")

print(f"This project was started in {HPscarf.startdate} and is a {HPscarf.crafttype} project and has a status of {HPscarf.status}.")

#MUTATING STATES 
# to change an attribute you can 

class UnfinishedProject():
    type = "Unfinished Craft Project"
    status = "WIP"

    def __init__(self,start_date,craft_category):
        # these are INSTANCE attributes
        self.startdate = start_date
        self.crafttype = craft_category
    
    def change_status(self, newstatus):
        self.status = newstatus

HPscarf = UnfinishedProject("Jan 2019","knitting")

print(f"This project has a status of {HPscarf.status}.")

HPscarf.change_status("Finished")

print(f"This project has a status of {HPscarf.status}.")

### __STR__ method

# Like __init__, every class has a __str__ method as default, stating how the class should be represented as a string e.g. 
# ---> <_main_.ObjectName object at 0dmf3fh>

# we can customise this:

class UnfinishedProject():
    type = "Unfinished Craft Project"
    status = "WIP"

    def __str__(self):
        return f"<An unfinished project of type {self.type}>"

socks = UnfinishedProject()

print(socks)