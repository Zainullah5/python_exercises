# Problem 1
# Write a Python function that accepts two integer numbers.
# If the product of the two numbers is less than or equal to 1000, return their product; 
# otherwise, return their sum.

num1 = int(input('Enter first number :'))
num2 = int(input('Enter second number :'))
def Multiplication_or_sum(num1 , num2):
    product = num1  * num2
    if product<= 1000 :
        return f'product of {num1} and {num2} is :{product}'
    else :
        return f'sum of {num1} and {num2} is :{num1 + num2}'


print(Multiplication_or_sum(num1 , num2))