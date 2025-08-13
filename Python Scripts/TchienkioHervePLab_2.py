################################################################# 
# Class: CMSC135
# Instructor: McGowan Stephen
# Program Assignment: 2
# Program Name:      Assignment2.py
# Author:             Tchienkio Herve
# Due Date:               07/28/2024 
# Description: Give a brief description of each Program
#      I pledge that I have completed the programming assignment independently.
  	#     I have not copied the code from a student or any source.
 #  I have not given my code to any student.
  #   Print your Name here: TCHIENKIO
        
###################################################################


def main():
    # Prompt the user to enter a month (use the numeric form)
    month = int(input("Enter the month (in numeric form, e.g., 1 for January): "))
    
    # Prompt the user to enter a day
    day = int(input("Enter the day: "))
    
    # Prompt the user to enter a two-digit year
    year = int(input("Enter a two-digit year: "))
    
    # Determine if the date is magic
    if month * day == year:
        print("The date is magic!")
    else:
        print("The date is not magic.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
