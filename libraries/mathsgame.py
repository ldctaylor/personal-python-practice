# MATHS GAME
# Decide if you want to play easy, medium, hard. The level you choose determines the number of digits in the numbers you need to add together.

import time
from random import randint

def main():
    highspeed = 0 #set highspeed that persists for duration of the programme running
    level = get_level() #decide the level of the game 1,2,3 (determines number of digits in numbers)
    while True:
        t0 = time.time() 
        correct = play_game(level) #sets the number of questions answered correctly while playing the game
        t1 = time.time()
        speed = int(t1 - t0)
        print(f"Score: {correct} in {speed} seconds!")
        if (0 == highspeed) or (speed < highspeed):
            print("AND YOU GOT A FASTEST SPEED SCORE! WELL DONE!")
            highspeed = speed
        if input("Play again? y/n") != "y": 
            print(f"Thanks for playing! Your high score was {highspeed} seconds")
            break

def get_level(): # prompts user to input the level of game they wish to play
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except:
            pass

def generate_integer(level): # generate random numbers based on number of digits chosen (level)
    if level == 1:
        return randint(0,9)
    if level in [2,3]:
        return randint(10**(level-1),10**level-1)
    else:
        raise ValueError
    
def play_game(level):
    correct = 0 #tracks number of questions answred correctly
    for _ in range(1,11): #generate 10 maths questions
        x = generate_integer(level)
        y = generate_integer(level)
        i = 0
        while i <= 3: #user is allowed three attempts
            try:
                if x + y == int(input(f"{x} + {y} = ")):
                    correct += 1
                    break
                print("EEE")
            except:
                print("EEE")
            i += 1
            if i == 3:
                print(f"{x} + {y} = {x + y}")
                break
    return(correct)

if __name__ == "__main__":
    main()