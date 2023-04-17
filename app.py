# Python is fun i wanna learn everything
name = 'John Smith'
print(name)
age = '20 years'
print(age)
is_new = True

# #input from user
persons_name = input('what is your name ')
color = input('what is your favourite color? ')
print(persons_name +  ' likes '  + color)

# #to calculate the age
year_of_birth = input('Year of Birth:')
# int() used to convert string year_of_ birth to integer
age = 2023 - int(year_of_birth)
print(age)

# #string concatenation in python
# #first method is to use + sign and the str() function to convert integers into strings
print('There are ' + str(24) + ' hours in day ')

# #second method of string concatenation using the braces and f before the single quotes
# print(f'There are {24} hours in a day')

calculation_hours = 24
name_of_units = "hours"

#functions
#use keyword def to define function
#to start a function you need to leave a blank line before function definition
#num_of_days is the definition of function parameters

def days_to_units(num_of_days):
    print(f"{num_of_days} {num_of_days* calculation_hours } {name_of_units}")
#35 is a function parameter
days_to_units(35)
days_to_units(20)
days_to_units(30)
days_to_units(60)

print(f"20 days are {20 * calculation_hours } {name_of_units}")
print(f"30 days are {30 * calculation_hours } {name_of_units}")
print(f"40 days are {40 * calculation_hours } {name_of_units}")
print(f"50 days are {50 * calculation_hours } {name_of_units}")
print(f"60 days are {60 * calculation_hours } {name_of_units}")
