from sys import argv
#from os.path import exists

print('What is your name?', end=' ')
name = input()
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, your name is {name}, you're {age} years old, {height} cm tall and {weight} kg heavy.\n")

print("After this you need to open file and print\n")

# Opening test.txt

script, filename = argv

txt = open(filename)
print(txt.read())

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
indata = txt_again.read()

print(txt_again.read())
print(f"\nThe input file is {len(indata)} bytes long")
txt.close()
txt_again.close()
#


print('\nLet\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.\n')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------\n")


five = 4 - 2 + 4 - 1
print(f"This should be five: {five}\n")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("\nWith a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15


if people < cats:
    print ("\n\nToo many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("Too many dogs! The world is drooled on!")

if people > dogs:
    print("Too many people! The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
