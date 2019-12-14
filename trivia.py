#Assignment 1 - Trivia Program
#Anthony Swift

#Print heading
print("\nThe Trivia Program\n")

#Get users name
user_name = input("Please enter your name: ")

#Get users age
user_age = int(input("Please enter your age: "))

#Get users weight
user_weight = int(input("Please enter your weight in kilos: "))

#Welcome user
print("\nHi",user_name)
#Convert user's age in years to a number of seconds

seconds_in_year = 31536000
users_age_in_seconds = user_age * seconds_in_year

#Display user's age in seconds
print("Did you know?")
print("You are" ,users_age_in_seconds, "seconds old!")

#Calculate moon weight

earth_gravity = 9.81
moon_gravity = 1.622

moon_weight = (user_weight / earth_gravity) * moon_gravity

#Display moon weight

print("You would weigh" ,moon_weight, "kilos on the moon!")

#Calculate mars weight

mars_gravity = 3.711

mars_weight = (user_weight / earth_gravity) * mars_gravity

#Display mars weight

print("You would weigh" ,mars_weight, "on Mars!")

#Calculate venus weight

venus_gravity = 8.87

venus_weight = (user_weight / earth_gravity) * venus_gravity

#Display venus weight

print("You would weigh" ,venus_weight, "on Venus!\n")

#Calculate difference in weight between Earth and Moon

weight_difference = user_weight - moon_weight

#Display difference in weight between Earth and Moon

print(user_name, "here is some great advice....")
print("Fly to the moon and lose" ,weight_difference, "kilos!")




