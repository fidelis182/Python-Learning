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
#35 is a function parameter
# days_to_units(35)
# days_to_units(20)
# days_to_units(30)
# days_to_units(60)

#user inputs
number_of_days = input("Enter number od days\n")
#use int() in casting to convert a string to integer
input_number_of_days = int(number_of_days)
calculated_days = days_to_units(input_number_of_days )
print(calculated_days)
