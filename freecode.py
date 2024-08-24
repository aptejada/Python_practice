# Aubrey Joy P. Tejada
# Practice exercise using the FreeCode Camp

# 23 August 2024

number = 5 # create a variabke and assign the value 5
text = 'Hello World' # Another variable called text and assign a string 'Hello World'
print(text) # to print the text variable to the screen
print(text[6]) # print the character at index 6; index begins at 0
print(text[-1]) # negative means start at the end of the string
print(len(text)) # to print the number of characters in a string
print(type(text)) # to print the data type; a string

shift = 3
print(shift)
print(type(shift)) # an integer

alphabet = 'abcdefghijklmnopqrstuvwxyz'  # a new string
alphabet.find('z') # argument to find 'z'
alphabet.find(text[0]) # modified argument by an index
index = alphabet.find(text[0]) # set variable called index
print(index) # returns the position or index of the letter z

# .find() returns the index of the matching character inside the string.
 # if the character is not found, it returns -1. As you can see, the first character in 
 # text, uppercase 'H', is not found, since alphabet
 # contains only lowercase letters

 # You can transform a string into its lowercase equivalent with the .lower() method. Add another print() call to print text.lower()
 # and see the output

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

index = alphabet.find(text.lower()[0])
print(text.lower())
print(index)

# returned hello world and 7
#We have liftoff!

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

index = alphabet.find(text[0].lower())
print(index)

# returned 7

# Step 19
# Declare a new variable named shifted. 
# Use the bracket notation to access the value of alphabet at index index and assign it to your new variable 

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

index = alphabet.find(text[0].lower())

shifted = alphabet[index]

print(index)

# Step 20
# Print your shifted

print(shifted)

#it returned 7 and h

baz luhrmann books about geography


# Step 21
# As you can see from the output, 'h' is at index 7 in the alphabet string. 
# Now you need to find the letter at index 7 plus the value of shift. 
# For that, you can use the addition operator, +, in the same way you would use it for a mathematical addition.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)

shifted = alphabet[index + shift]

print(shifted)

# returned k (7 + 3)

# Step 22
# Repeating the process of locating the letter inside the alphabet and determine the shifted letter for each character in text can be tedious. 
# Thankfully, you can simplify it using a loop.

# For now, remove all the lines of code below the declaration of the alphabet variable.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for loop
# for i in text
# for is the keyword denoting the loop type. 
# i is a variable that sequentially takes the value of the elements in text. 
# The statement ends with a colon, :.

# Below the line where you declared alphabet, 
# write a for loop to iterate over text. Use i as the loop variable.

for i in text

# Step 24
# The code to execute at each iteration — placed after the : 
# — constitutes the body of the loop. This code must be indented. 
# In Python, it is recommended to use 4 spaces per indentation level. 
# This indented level is a code block.

#Python relies on indentation to indicate blocks of code. 
# A colon at the end of a line is a signal that a new indented block of code will follow.

#So, when no indented block is found after the final colon, the code execution stops and an IndentationError is thrown. 
# This code will not show the output and instead raise an IndentationError:

# Give your for loop a body by adding a call to print(i). 
# Remember to indent the loop body.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in text:
    print(i)

# it gives a series of hello world strings arranged vertically

# remember that i and iteration variable can have any valid nae, 
# but it is convenient to give it a meaningful name
# 
# Renae your i variable to char

for char in text:
    print(char) # this returns letters written singly/vertically

# Step 26
# Inside the for loop, before printing the current character, 
# declare a variable called index and assign the value returned by alphabet.find(char)
# to this variable.

for char in text:
    index = alphabet.find(char)
    print(char)

# Currently, the print() function is taking a single argument char, 
# but it can take multiple arguments, separated by a comma.

# Add a second argument to print(char) so that it prints the character and its index inside the alphabet.

for char in text:
    index = alphabet.find(char)
    print(char, index) # prints both chat and assigned index per letter


# notice however that H returned -1 index; remember that H is not capitalized in the alphabet variable

# Step 28
# find is again returning -1 for uppercase letters, and for the space character, too. 
# You are going to take care of the space later on.

# For now, instead of iterating over text, change the for loop to iterate over text.lower().

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)

    text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Step 29
# At the end of your loop body, 
# declare a variable called 
# new_index and assign the value of index + shift to this variable.

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift

# Step 30
# Strings are immutable, 
# which means they cannot be changed once created. 
# For example, you might think that the following code 
# changes the value of my_string into the string 'train', but this is not valid:

# this ones invalid
text = 'Hello World'
text[0] = 'B' # returned a TypeError message
