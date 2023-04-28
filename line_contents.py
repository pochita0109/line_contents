# Kenneth John Costa
# Assignment 4
# Writing multiple line of text contents

# Write a method in python to write multiple line of text contents 
# into a text file mylife.txt.

def line():
# Open a txt file called mylife.txt
    with open("mylife.txt", "a") as output_file: 
# Ask the user to write a line
     lines = input("\033[93mEnter line:\033[1m ")
# Write the line entered by user
     output_file.write(lines + "\n")
line()
# Ask the user if they want to continue on writing lines
while True:
     answer = input("\033[94mAre there more lines? y/n:\033[0m ")
# If yes:
     if answer == "y":
        line()
# If no:
     elif answer == "n":
        print("\033[92mThe lines that you have entered are now saved")
        exit()
# If outside on choices:
     else:
        print("Invalid Answer")