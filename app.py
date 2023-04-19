# Python is fun i wanna learn everything
# name = 'John Smith'
# print(name)
# age = '20 years'
# print(age)
# is_new = True

# #input from user
# persons_name = input('what is your name ')
# color = input('what is your favourite color? ')
# print(persons_name +  ' likes '  + color)

# #to calculate the age
# year_of_birth = input('Year of Birth:')
# int() used to convert string year_of_ birth to integer
# age = 2023 - int(year_of_birth)
# print(age)

# #string concatenation in python
# #first method is to use + sign and the str() function to convert integers into strings
#

# #second method of string concatenation using the braces and f before the single quotes
# print(f'There are {24} hours in a day')

calculation_hours = 24
name_of_units = "hours"

#functions
#use keyword def to define function
#to start a function you need to leave a blank line before function definition
#num_of_days is the definition of function parameters

def days_to_units(num_of_days):
 return f"{num_of_days} {num_of_days* calculation_hours } {name_of_units}"
def valiadte_input():
     try :

        number_input = int(number_of_days)
        if number_input > 0:
            calculated_value = days_to_units(number_input)
            print(calculated_value)
        elif number_input == 0:
             print("number entered is 0")
        else:
            print("The number entered is a negative number")
     except ValueError:
        print("the input is invalid")
#user inputs
number_of_days = input("Enter number of days\n")
valiadte_input()


