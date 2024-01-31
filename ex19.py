def cheese_and_crackers(cheese_count, boxes_of_crackers): #Define a function name cheese_and_crackers
    print(f"You have {cheese_count} cheeses!") #Print a formatted string with variable cheese_count
    print(f"You have {boxes_of_crackers} boxes of crackers!") #Print a formatted string with variable boxes_of_crackers
    print("Man that's enough for a party!") #Regular print tho
    print("Get a blanket.\n") #Same but closed with a new line

print("We can just give the function numbers directly:") #Print a string
cheese_and_crackers(20, 30) #Call the function

print("We can use variables from our script:") #Print a string
amount_of_cheese = 10 #Assigne a value of 10 to variable amount_of_cheese
amount_of_crackers = 50 #Assigne a value of 50 to variable amount_of_crackers

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #Call the function

print("We can even do math inside too:") #Print a string
cheese_and_crackers(10 + 20, 5 + 6) #Call the function

print("And we can combine the two, variables and math:") #Print a string
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #Call the function
