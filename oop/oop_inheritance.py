#define a superclass
class super_class:
    #attributes and method definition
    pass

#inheritance
class sub_class(super_class):
    #attributes and method of super_class
    #attributes and method of sub_class
    pass

##MULTIPLE inheritance
class SuperClass1:
    #features of superclass 1
    pass
class SuperClass2:
    #features of superclass 2
    pass
class MultiDerived(SuperClass1, SuperClass2):
    #features of SuperClass1 + SuperClass2 _ MultiDerived class
    pass

#----------------Example
# base class
class Animal:
    def eat(self):
        print("I can eat!")
    
    def sleep(self):
        print("I can sleep!")

#derived class
class Dog(Animal):
    def bark(self):
        print("Woof!")

#Create a dog object
Annie = Dog()

#Create an animal object
Kitty = Animal()

#Calling members of the base class
Annie.eat()
Annie.sleep()
Annie.bark()
Kitty.bark() # <--- AttributeError "Animal" has no attribute 'bark'

