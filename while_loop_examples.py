-# While Loop Example 1
# Print numbers from 1 to 5

i = 1
while i <= 5:
    print(i)
    i += 1


# While Loop Example 2
# Print even numbers from 2 to 10

i = 2
while i <= 10:
    print(i)
    i += 2


# While Loop Example 3
# Print numbers from 10 to 1 (reverse order)

i = 10
while i >= 1:
    print(i)
    i -= 1


# While Loop Example 4
# Using break in while loop

i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1


# While Loop Example 5
# Using continue in while loop

i = 1
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i)