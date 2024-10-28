from PIL import Image
from rembg import remove
# input_path = "/home/wtc/Documents/side pojs/remove picture background/jpg-to-png/20230813_182643.jpg"
input_path = input("Please enter a path:  ")
 
from time import sleep
import sys

print("\n")

for i in range(21):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(0.25)

print("\n")
# 
filename = input("what would you like to name your file: ")
output_path = f"{filename}.png"
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

print("you can refresh and check for the file")
