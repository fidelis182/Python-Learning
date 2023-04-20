prices = [10,20,30]
sum = 0
for total in prices:
    sum += total
print(sum)
#nested for loop
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#challenge
numbers = [2,2,2,2,5]
for i in numbers:
    output = ''
    for count in range(i):
        output += 'x'
    print(output)