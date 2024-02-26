def add(a, b): #Define a function name add
    print(f"ADDING {a} + {b}") #Print a formatted string
    return(a + b) #Return a + b

def subtract(a, b): #Define a function name subtract
    print(f"SUBTRACTING {a} - {b}") #Print a formatted string
    return(a - b) #Return a - b

def multiply(a, b): #Define a function name multiply
    print(f"Multiplying {a} * {b}") #Print a formatted string
    return(a * b) #Return a * b

def divide(a, b): #Define a function name divide
    print(f"Dividing {a} / {b}") #Print a formatted string
    return(a / b) #Return a / b

print("Let's do some math with just functions:") #Print a string

age = add(30, 5) #Call the function
height = subtract(78, 4) #Call the function
weight = multiply(90, 2) #Call the function
iq = divide(100, 2) #Call the function

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}") #Print a formatted string

# A puzzle for the extra credit, type it anyway.
print("Here is a puzzle.") #Print a string

what = add(age, subtract(height, multiply(weight, divide(iq,2)))) #Call the function

print("That becomes: ", what, "Can you do it by hand?") #Print a string