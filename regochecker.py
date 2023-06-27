# Implement a program that prompts the user for a rego plate and outputs valid if meets all of the requirements or invalid if it does not. 
# Assume any letters in the user’s input will be uppercase. 
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
# “All plates must start with at least two letters.”
# Plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    #Debugging:
    # print(f"is_two_letters is{is_two_letters(s)}")
    # print(f"are_numbers_at_end is {are_numbers_at_end(s)}")
    # print(f"is_chars_count is {is_chars_count(s)}")
    # print(f"valid_chars is {valid_chars(s)}")
    # print(f"is_valid is {is_valid(s)}")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if not is_two_letters(plate):
        return False
    if not are_numbers_at_end(plate):
        return False
    if not is_chars_count(plate):
        return False
    if not valid_chars(plate):
        return False
    return True

def is_chars_count(s):
    return 2 <= len(s)<= 6 #needs to return true

def is_two_letters(s):
    return s[0:2].isalpha()

def are_numbers_at_end(s):
    if plate.isalpha():
        return True
    for index in range(len(s)-1):
        if plate[index].isalpha():
            if plate[index+1] == "0": #checks first digit is not 0
                return False
        else:
            for char in s[index+1:len(s)]: #checks the subsequent character is not alpha
                if char.isalpha():
                    return False
            return True

def valid_chars(s):
    if s.isalnum() == False:
        return False
    return True

main()

