cars = 100 #Create variable car with 100 value probably float
space_in_a_car = 4.0 #Create space in car variable so we knew the capacity for that car
drivers = 30 #Create variable drivers with value 30
passangers = 90 #Create variable passangers with value 90
cars_not_driven = cars - drivers #Create variable cars_not_driven with value of car - drivers
cars_driven = drivers #Indicate that cars_driven is driven by a total of driver
carpool_capacity = cars_driven * space_in_a_car #Create variable carpool_capacity with value of cars_driven * space_in_a_car
average_passangers_per_car = passangers / cars_driven #Show average_passangers_per_car with value of passangers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passangers, "to carpool today.")
print("We need to put about", average_passangers_per_car, "in each car.")