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

#to calculate the age
year_of_birth = input('Year of Birth:')
# int() used to convert string year_of_ birth to integer
age = 2023 - int(year_of_birth)
print(age)

#string concatenation in python
#first method is to use + sign and the str() function to convert integers into strings
print('There are ' + str(24) + ' hours in day ')

#second method of string concatenation using the braces and f before the single quotes
print(f'There are {24} hours in a day')
