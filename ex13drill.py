from sys import argv
# read the WYSS section for how to run this
script, name, degree, skill = argv

print("The script is called:", script)
print("Your name is:", name)
print("Your are a ", degree, "degree")
print("Your have a", skill, "skill")

input("Press Enter to continue...")
likes = input("What do you like? ")
print("So you had a", likes, "in your life and the you get your", degree, "degree.")