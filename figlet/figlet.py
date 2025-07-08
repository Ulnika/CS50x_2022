import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    inp = input("Input: ")
    figlet.setFont(font=random.choice(fonts))
    print("Output:")
    print(figlet.renderText(inp))

elif (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in fonts):
        inp = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output:")
        print(figlet.renderText(inp))
else:
    sys.exit("Invalid usage")