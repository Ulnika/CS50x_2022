import sys
import csv
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

filename1 = sys.argv[1].split(".")
filename2 = sys.argv[2].split(".")

if filename1[1] not in ["jpg", "jpeg", "png"]:
    sys.exit("Invalid input")
if filename2[1] not in ["jpg", "jpeg", "png"]:
    sys.exit("Invalid input")
if filename1[1] != filename2[1]:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    inp = Image.open(sys.argv[1])
    inp_resized = ImageOps.fit(inp, shirt.size)

    inp_resized.paste(shirt, shirt)

    inp_resized.save(sys.argv[2])



except FileNotFoundError:
    sys.exit("Input does not exist")