# Problem 1
# Write a Python function that accepts two integer numbers.
# If the product of the two numbers is less than or equal to 1000, return their product; 
# otherwise, return their sum.

def Multiplication_or_sum(num1 , num2):
    product = num1  * num2
    if product<= 1000 :
        return f'product of {num1} and {num2} is :{product}'
    else :
        return f'sum of {num1} and {num2} is :{num1 + num2}'


print(Multiplication_or_sum(20 , 30))

print(Multiplication_or_sum(40 ,30))