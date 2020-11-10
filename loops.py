# Loops and iterations (For and while loops)
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# Looking for a value and breaking the loop
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

# Looking for a value and continuing the loop
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# Loop within a loop example
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Built in function range to go through a loop x amount of times
for x in range(1, 11):
    print(x)

# While loops keep going until a condition or a break is met
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
