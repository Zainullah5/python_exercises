# Display only those characters which are present at an even index number in given string.

# Method No 1
print('Method No 1 \n using for loop')
text = input('Enter your string :')

for i in range(len(text)):
    if i % 2 == 0 :
        print(text[i] , end='')

# for next line 
print('')

## Method No 2
print('Method No 2 \n using string slicing ')
s = input("Enter a string: ")

print(s[::2])


