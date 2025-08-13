################################################################# 
# Class: CMSC135
# Instructor: Prof. Stephen McGowan
# Program Assignment: 1
# Program Name:      Assignment1.py
# Author:             Student Tchienkio Herve
# Due Date:               06/18/2024 
# Description: Give a brief description of each Program
#      I pledge that I have completed the programming assignment independently.
  	#     I have not copied the code from a student or any source.
 #  I have not given my code to any student.
  #   Print your Name here: Herve TCHIENKIO
            
###################################################################

# Personal information
name = "Herve TCHIENKIO"
address = "17600 Sequoia Dr, Gaithersburg, Maryland, 20877"
phone_number = "240-810-8143"
college_major = "Cybersecuty"

# Cookie recipe ingredients for 48 cookies
sugar_cups = 1.5
butter_cups = 1.0
flour_cups = 2.75
cookies_per_batch = 48

# Function to calculate ingredient amounts based on desired number of cookies
def calculate_ingredients(num_cookies):
    factor = num_cookies / cookies_per_batch
    sugar_needed = sugar_cups * factor
    butter_needed = butter_cups * factor
    flour_needed = flour_cups * factor
    return sugar_needed, butter_needed, flour_needed

# Display personal information
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Phone Number: {phone_number}")
print(f"College Major: {college_major}")

# Get the number of cookies the user wants to bake
num_cookies = int(input("How many cookies do you want to bake: "))

# Calculate and display the required ingredients
sugar_needed, butter_needed, flour_needed = calculate_ingredients(num_cookies)
print(f"\nTo bake {num_cookies} cookies, you will need:")
print(f"{sugar_needed:.2f} cups of sugar")
print(f"{butter_needed:.2f} cups of butter")
print(f"{flour_needed:.2f} cups of flour")
