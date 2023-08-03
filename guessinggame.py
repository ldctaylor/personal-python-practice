import random

print("\nWelcome to my guessing game!")
print("I'm going to think of a number between 1 and what you tell me the highest option should be.")
print("Give me the highest number I should guess to:")
while True:
    try:
        value = int(input("Guess from 1 to:"))
        if value > 0:
            break
    except:
        pass

#randint(1,100) equivalent to randrange(1,101)
number = random.randint(1, value)
print("Great, now it's time for you to guess.")

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > number:
                print("Too large!")
            if guess < number:
                print("Too small!")
            if guess == number:
                print("Just right!")
                break
    except:
        pass
