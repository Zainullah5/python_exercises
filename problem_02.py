# Iterate through the first 10 numbers (0–9).
# In each iteration, print the current number, the previous number, and their sum.

num = int(input('Enter your number :'))
pervious_number = 0

for  i in range(1 , num+1):
    sum =  i + pervious_number
    print(f'Current Number {i} Previous Number {pervious_number}  Sum:{sum} ')
    pervious_number = i