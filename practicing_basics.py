#I'm just practicing basic skills learnt. I've put various beginner101 practices here but put them together so that the user is prompted to specify which one he wants to run at the command line.

#defining my exercise list as a global variable.
exerciselist = ["emojis", "service charge", "quieten down", "douglas adams"]

def main():
    #Prompt the user to specify the exercise they'd like demonstrated. My ability to validate input is still pretty limited but I have stripped leading or trailing whitespace and forced lowercase so that the input is treated case insensitively.
    chosen_exercise = (input("Please specify which of the exercises you would like to experience. The choices are " + str(exerciselist)[1:-1] + ": ")).strip().casefold()
    #select the chosen exercise
    match chosen_exercise:
        case "emojis":
            run_emojis()
        case "service charge":
            calculate_service()
        case "quieten down":
            pass #STILL TO COME
        case "douglas adams":
            pass #STILL TO COME
        case _:
            print("Sorry, I did not understand your input. I'm spontaneously combusting.")

#Define the methods to run the demos.

#1. run_emojis
#run_emojis converts old school emotions entered using keyboard symbols (only :) and :( ) into emojis
def run_emojis():
    cavemantext = input("Give me some emotion, old school style ;-P ")
    teentext = convert_input_to_teenspeak(cavemantext)
    print(teentext)

def convert_input_to_teenspeak(cavemantext):
    teentext = cavemantext.replace(":)","🙂").replace(":(","🙁")
    return teentext

#2. calc_service_charge
#calculate_service() asks the user for the cost of the service and how much they'd like to add on as a tip, and then prints the amount they should tip to two decimal places

def calculate_service():
    #Prompts user to ask for the cost, and how much they'd like to add on as a tip
    #Then converts these values into floats, and the percent value into a decimal
    dollars = float(input("How much was the cost of the meal / haircut / service? ").strip("$"))
    percent = float(input("What percentage would you like to tip? ").strip("%")) / 100
    tip = dollars * percent
    print(f"To leave {round(percent*100,1)}% tip, you should leave ${tip:.2f}")

main()