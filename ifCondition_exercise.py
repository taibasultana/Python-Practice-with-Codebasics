#Write a program that can tell you your BMI Category.
#Ask user to enter height
#Ask user to enter weight
#Calculate the BMI(Body Mass Index = weight / height 2) and store it in a variable
#If the BMI is 30 or greater, print “Obesity”
#If the BMI is in between 25 and 29, print “Overweight”
#If the BMI is in between 18.5 and 25, print “Normal”
#If the BMI is less than 18.5, print “Underweight”

# h=input("Enter height:")
# h=int(h)
# w=input("Enter weight:")
# w=int(w)
# Body_Mass_Index=w/h**2
# print("BMI",w/h**2)
#
# if Body_Mass_Index>=30:
#     print("Obesity")
# elif 25>Body_Mass_Index>29:
#     print("Overweight")
# elif 18.5>Body_Mass_Index>25:
#     print("Normal")
# elif 18.5>Body_Mass_Index:
#     print("Underweight")
# else:
#     print("Null")


#India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#USA = ["New York","Chicago","Las Vegas", "San Francisco"]
#UK = ["London", "Manchester", "Liverpool", "Nottingham"]
#Write a program that asks the user to enter a city name, and it should tell which country the city belongs to
#Write a program that asks users to enter two cities, and it tells you if they both are in the same country or nor />
#For example:
#If I enter Mumbai and Chennai, it will print "Both cities are in India"
# but if I enter Mumbai and New York it should print "They don't belong to the same country"

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]
city=input("Enter a city name:")
if city in India:
    print(f"{city} is India")
elif city in USA:
    print(f"{city} is USA")
elif city in UK:
    print(f"{city} is UK")
else:
    print("Null")

city1=input("Enter city name:")
city2=input("Enter another city name:")
if city1 and city2 in India:
    print(f"Both city1 and city2 are in India ")
elif city1 and city2 in USA:
    print(f"Both city1 and city2 are in USA ")
elif city1 and city2 in UK:
    print(f"Both city1 and city2 are in UK ")
else:
    print("They don't belong to the same country")

