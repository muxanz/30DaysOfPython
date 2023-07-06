# Day 2: 30 Days of Python programming
import math

first_name = "Paco"
last_name = "Paraco"
full_name = "Paco Paraco"
country = "Mexico"
city = "Tijuana"
age = 35
year = 2023
is_married = False
is_true = True
is_light_on = False

brand, model, serial_number = "Samsung", "F27T350FHL", 500291


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(brand))
print(type(model))
print(type(serial_number))

print(len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
exp1 = pow(num_one, num_two)
floor_division = num_one // num_two

radius = int(input("Input radius: "))
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * radius * math.pi 

print(area_of_circle, circum_of_circle)

user_first_name = input("User first name: ")
user_last_name = input("User last name: ")
user_country = input("User country: ")
user_age = int(input("User age: "))

help("keywords")