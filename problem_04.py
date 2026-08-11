# Write a function to remove 
# characters from a string starting from index 0
#  up to n and return a new string.

def func(wrod , n):
    return wrod[n:]

string = input('Enter your text :')
print(func(string,3))