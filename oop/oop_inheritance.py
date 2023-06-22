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

