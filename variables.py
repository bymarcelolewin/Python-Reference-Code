day = 25
day_name = "Tuesday"
month = 'October'
temp = -15

print(f"Today is {day_name}, {month} {day} and it's {temp} degrees outside.")


light_is_on = True
water_is_off = False
message = "off"

if light_is_on:
    message = "on"

print(f"Light is {message}.")

age = 17

if age >= 18:
    print("You are an adult!")
else:
    print("You are a child!")


import random

print(random.randint(1, 10))
print(random.random())