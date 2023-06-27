def main():
    s = input("Plate: ")
    #Debugging:
    # print(f"is_two_letters is{is_two_letters(s)}")
    # print(f"are_numbers_at_end is {are_numbers_at_end(s)}")
    # print(f"is_chars_count is {is_chars_count(s)}")
    # print(f"valid_chars is {valid_chars(s)}")
    # print(f"is_valid is {is_valid(s)}")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not is_two_letters(s):
        return False
    if not are_numbers_at_end(s):
        return False
    if not is_chars_count(s):
        return False
    if not valid_chars(s):
        return False
    return True

def is_chars_count(s):
    return 2 <= len(s)<= 6 #needs to return true

def is_two_letters(s):
    return s[0:2].isalpha()

def are_numbers_at_end(plate):
    if plate.isalpha():
        return True
    for index in range(len(plate)-1):
        if plate[index].isalpha():
            if plate[index+1] == "0": #checks first digit is not 0
                return False
        else:
            for char in plate[index+1:len(plate)]: #checks the subsequent character is not alpha
                if char.isalpha():
                    return False
            return True

def valid_chars(plate):
    if plate.isalnum() == False:
        return False
    return True

main()

