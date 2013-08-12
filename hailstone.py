# Generate a hailstone sequence
number_str = input("Enter a positive integer:")
number = int(number_str)
count = 0

print("Starting with number:",number)
print("Sequence is: ", end=' ')

while number > 1: # stop when the sequence reaches 1

    if number % 2:              # if number is odd..
        number = number * 3 + 1 # we take that number, multiply by three, add 1
    else:                       # if the number is even..
        number = number / 2     # we take THAT number and divide by 2
    print(number,",", end=' ')  # we then add the number to the sequence

    count += 1                  # add to the count

else:
    print()                     # print a blank line so that it's pretty
    print("Sequence is ",count," numbers long")
        
