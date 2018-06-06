cars = 100 # the number of cars available
space_in_a_car = 4.0 # the amount of available seats in each car
drivers = 30 # the number of people who can drive
passengers = 90 # the number of people who need a driver and a car
cars_not_driven = cars - drivers #the difference of total cars and drivers
cars_driven = drivers #the amount of cars driven equals the number of drivers
carpool_capacity = cars_driven * space_in_a_car
# ^ The total number of passengers that can get a ride
# The average number of people that need to be in each car to transport them all
average_passengers_per_car = passengers / cars_driven


print("The are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have" , passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, 'in each car.')


#Study Drills, The code referenced on page 47 of lpthw is incorrect as
#car_pool_capacity is not the same as carpool_capacity, the "_" symbol is treated
# as part of the variable
# With line 2 if just a 4 is used instead of 4.0 then answers that are created
#by any expression that variable is used in will be
#whole integers unless the "/" function is used. With this specific program in
#mind it doesn't matter. Floats are more accurate, but depending on situation
#can lead to bugs.
# 2.) Check
# 3.) Check
# 4.) "=" assigns data a name. "==" is a logical check that sees if they are equal
#5.) "_" underscore is a valid character
# 6.) I learned that if x = 6 and i = 7 you can make x = 7 by writing
# x = i. Conversely you can write i = x to make i = 6.
# The first character written -- "i" in i = 7 -- will have the value assigned to
#it. Order matters a lot.
