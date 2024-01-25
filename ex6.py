types_of_people = 10 #Assigne a value of 10 to variable types_of_people
x = f"There are {types_of_people} types of people." #Assign a string to variable x

binary = "binary" #Assign a string to variable binary
do_not = "don't" #Assign a string to variable do_not
y = f"Those who know {binary} and those who {do_not}." #Assign a string to variable y

print(x) #Print variable x
print(y) #Print variable y

print(f"I said: {x}") #Print string with variable x
print(f"I also said: '{y}'") #Print string with variable y

hilarious = True #Assign a boolean value to variable hilarious
joke_evaluation = "Isn't that joke so funny?! {}" #Assign a string to variable joke_evaluation with variable hilarious inside it

print(joke_evaluation.format(hilarious)) #Print string with variable hilarious

w = "This is the left side of..." #Assign a string to variable w
e = "a string with a right side." #Assign a string to variable e

print(w + e) #Print string with variables w and e 