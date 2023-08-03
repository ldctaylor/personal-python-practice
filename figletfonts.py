import sys
from pyfiglet import Figlet
import random

# Requires installation of pyfiglet library, see requirements.txt

#list of fonts available needed for random font selection
fontlist = Figlet().getFonts()

#Error Handling - collected this in one place
# Accepted command lines will be EITHER python filename [-f or --font] fontname OR python filename
if len(sys.argv) not in [1,3]:
    sys.exit("Incorrect number of arguments")
if len(sys.argv) == 3:
    if sys.argv[1] not in ['-f','--font']:
        sys.exit("Incorrect syntax")
# capture cases where specified font is not found in font list
    if sys.argv[2] not in fontlist:
        sys.exit("Font not found")

if len(sys.argv) == 3:
    f = Figlet(font=sys.argv[2])
# if no additional arguments supplied, assign a random font
if len(sys.argv) == 1:
    f = Figlet(font=random.choice(fontlist))

print("\nWelcome to the figlet font generator!\n")
text = input("Write the text you'd like to see in figletfont: ")
print(f"\nOk your wish is my command....\n{f.renderText(text)}")
print("So long, and thanks for all the fish!\n")