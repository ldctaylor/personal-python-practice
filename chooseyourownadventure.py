#Just a little story game for the kids

def main():
    #get inputs for the story
    number = input("number between 10 and 99")
    noun1, noun2, noun3, noun4, noun5 = input("Give me 5 nouns please separated only by a space each: ").split(" ")
    transport = input("Give me a type of transportation")
    place = input("Give me a place")
    feeling = input("Give me a feeling")
    adj1, adj2 = input("Give me two adjectives separated by a space :").split(" ")
    food = input("Type of food, plural")
    word = input("Give me a silly word")
    verb1, verb2, verb3 = input("Give me 3 action verbs separated by a space ").split(" ")
    verb4, verb5 = input("Give me two past tense action verbs separated by a space").split(" ")
    room1, room2 = input("Give me 2 rooms separated by a comma: ").split(",")
    body = input("Give me a body part")
    exclamation = input("Give me an exclamation")
    icky = input("Give me something icky")

    #print the story
    print("It was the year 20",number,"and I was so excited to finally be receiving a",noun1,". In order to get it, I had to go to the",place,"using the",transport,".")
    print("As I arrived I felt so ",feeling,". In front of me was a",adj1,noun2,"and a sign pointing me to a",room1,". As I began walking my ",body,"began to ",verb1,". I",verb4,"and ",verb5,"towards the ",noun3,"that I suddenly spied in front of me.")
    print("Just then I heard a loud",exclamation,"that appeared to come from the",room2,". As I looked towards it I noticed a",adj2,noun4," with a label on it that said",word,".")
    print("This is",icky,"! I said, and decided to",verb2,"to the ",noun5,". Thankfully there was a big plate of ",food," there and I decide to ",verb3, "as far away from the",place," as I could.")
    print("The End")

main()
