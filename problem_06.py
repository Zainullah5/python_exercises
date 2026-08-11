num = int(input('Enter your Number :'))

factorial = 1

for i in range(1,num + 1):

    factorial = i * factorial

print(f"The factorial of {num} is {factorial}")