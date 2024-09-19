# Aubrey Joy P. Tejada
# Practice exercise using the FreeCode Camp

# 23 August 2024

number = 5 # create a variabLe and assign the value 5
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


# Step 31
# strings do not support item assignment, 
# because they are immutable. 
# However, a variable can be reassigned another string:

# Delete the text[0] line and reassign text the string 'Albatross'.

text = 'Hello World'
text = 'Albatross'

# I removed the text assigned before the string Albatross

# Step 33
# Now you need to create a new_char variable at the end of your loop body. 
# Set its value to alphabet[new_index].

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
    new_char = alphabet[new_index] # this adds three spaces (which is counted as char and a value of shift variable)


# now print the new_char
print(new_char)

# Step 35
# Clean the output a bit. 
# Delete print(char, index), and turn the last 
# print() call into 
# print('char:', char, 'new char:', new_char).

# it cleaned the table!

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]
    print('char:', char, 'new char: ', new_char)


# Step 36
# At the moment, the encrypted character is updated in every iteration. 
# It would be better to store the encrypted string in a new variable. 
# Before your for loop, declare a variable called encrypted_text and assign an empty string ('') to this variable.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

encrypted_text = ''
for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]
    print('char:', char, 'new char:', new_char)

# Step 37
# Now, replace new_char with encrypted_text. 
#  Also, modify the print() call into print('char:', char, 'encrypted text:', encrypted_text) to reflect this change.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

encrypted_text = ''
for char in text.lower():
    index = alphabet.find(char)    
    new_index = index + shift
    encrypted_text = alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

# Step 38
# Instead of assigning alphabet[new_index] to encrypted_text, 
# assign the current value of encrypted_text plus alphabet[new_index] to this variable.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = encrypted_text + alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

# Step 39
# You can obtain the same effect of a = a + b by using the addition assignment operator:

# Example Code
# a += b
# The addition assignment operator enables you to add a value to a variable and then assign the result to that variable.

# Use the += operator to add a value and assign it at the same time to encrypted_text.


shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text +=  alphabet[new_index] #added here; observe the previous argument
    print('char:', char, 'encrypted text:', encrypted_text)


# Step 40
# Comparison opertors 
# At the beginning of your loop body, 
# print the result of comparing char with a space (' '). Use the equality operator == for that.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower(): # convert text to lower text to match the alphabet
    print(char == ' ')    # print the result of comparing char with a space
    index = alphabet.find(char)
    new_index = index + shift # len(alphabet) # ensure the index wraps around
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)


# Step 41

# Currently, spaces get encrypted as 'c'
# To maintain the original spacing in the plain message, 
# you'll require a conditional if statement
# This is composed of the if keyword, a condition, and a colon :

# example: 
if x !=0
    print(x)

# In the example above, 
# the condition of the if statement is x != 0. 
# The code print(x), inside the if statement body, 
# runs only when the condition evaluates to True (in this example, meaning that x is different from zero)

# At the top of your for loop, 
# replace print(char == ' ') with an if statement. 
# The condition of this if statement should evaluate to True if char is an empty space and False otherwise. 
# Inside the if body, print the string 'space!'. 
# Remember to indent this line.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''


for char in text.lower():
    if char == ' ':
        print('space!')
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

    # the space between hello world now has space!

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ' '

for char in text.lower():
    if char == ' ':
        encrypted_text += char # add the space to encrypted_text
    index = alphabet.find(char)
    new_index = index + shift 
    encrypted_text += alphabet [new_index]
    print('char:', char, 'encrypted text:', encrypted_text)


# Step 43
# A conditional statement can also have an else clause. 
# This clause can be added to the end of an if statement to execute alternative code if the condition of the if statement is false

# Example

if x !=0:
    print (x)
else:
    print('x = 0')

#As you can see in your output, 
# when the loop iterations reach the space, 
# a space is added to the encrypted string. 
# Then the code outside the if block executes and a c 
# is added to the encrypted string


# To fix it, add an else clause after encrypted_text += 
# char and indent all the subsequent lines of code except the print() call.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower(): # rememeber you can change char into aby variable like i ; iteration
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = index + shift
        encrypted_text +=   alphabet  [new_index]
   
    print('char:', char, 'encrypted text:', encrypted_text)


# Step 44
# Try to assign the string 'Hello Zaira' to your text variable and see what happens in the terminal.
# You'll see a string index out of range exception. Don't worry, you'll figure out how to fix it soon!

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char #observe the encrypted text
    else:
        index = alphabet.find(char)
        new_index = index + shift
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

# this returns an error

# Step 45
# When the loop reaches the letter Z, 
# the sum index + shift exceeds the last index of the string alphabet. 
# Therefore, alphabet[new_index] is trying to use an invalid index, which causes an IndexError to be thrown.

# You can notice that the output in the terminal stops at the space immediately before the Z, 
# the last print before the error is thrown.

# In this case, 
# the modulo operator (%) 
# can be used to return the remainder of the division between two numbers. 
# For example: 
# 5 % 2 is equal to 1, because 5 divided by 2 has a quotient of 2 and a remainder of 1.


# 
text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ': # handle spaces; preserve spaces in the encrypted text
        encrypted_text += char
    else:           # encrypt non space characters
        index = alphabet.find(char)
        new_index = (index + shift) % 26 # modulo ensures that if the new index goes beyond the end of the alphabet, it wraps around the beginning
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

# Step 46
# If you wish to incorporate additional characters into the alphabet string, 
# such as digits or special characters, 
# you'll find it's necessary to manually modify the right operand of the modulo operation.

# Replace 26 with 
# len(alphabet) to avoid this issue

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet) # this is the part that has been modified
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

# Step 47
# Next, modify your print() call to print 
# 'encrypted text:', encrypted_text and put it 
# outside the for loop, so that the encrypted string is printed one time.

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len   (alphabet)
        encrypted_text += alphabet[new_index]
    print('char:', char)

print('encrypted text:',encrypted_text)

# Step 48
# Right before the print call, 
# add another one and pass 'plain text:', 
# text as the arguments to print(). 
# Use the same indentation.

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]

print('plain text:', text)
print('encrypted text:', encrypted_text)


# Step 49
# A function is essentially a reusable block of code. 
# You have already met some built-in functions, like print(), find() and len(). 
# But you can also define custom functions like this:

# Example
def function_name():
    <code>

# A function declaration starts with the def keyword followed by the function name — a valid variable name — and a pair of parentheses. 
# The declaration ends with a colon.

# Right after your shift variable, 
# declare a function called caesar and indent all the following 
# lines to give your new function a body.

text = 'Hello Zaira'
shift = 3

def caesar():

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)

# Step 50
# In Python, the scope of a variable determines where that variable can be accessed:

# Variables defined outside a function have a [ global scope ] and they can be accessed from any part of your code.
# Variables defined inside a function are [ local ] to that function and cannot be accessed outside of it.
# To see this in action, 
# try to print the alphabet variable at the end of your code. 
# This will raise a NameError exception.

# You should see an error message indicating that alphabet is not defined. 
# This is because alphabet is defined inside the caesar function and is not accessible outside of it.

text = 'Hello Zaira'
shift = 3

def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)
print(alphabet)

# Step 51
# Now, fix the error by removing the line that tries 
# to print the alphabet variable outside of the caesar function.

text = 'Hello Zaira'
shift = 3

def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)


# 52
# To execute, a function needs to be called (or invoked) by appending a pair of parentheses after its name, like this:

# Example Code

function_name()

# At the end of your code, 
# call your caesar function. 
# Pay attention to the indentation.

text = 'Hello Zaira'
shift = 3

def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)
caesar()

# 53 
# Now you should see the output again. 
# Although this approach works, 
# it doesn't significantly enhance the code's reusability. 
# Repeatedly calling your function will result in the same outcome. 
# However, functions can be declared with parameters to introduce versatility and customization:

def function_name(param_1, param_2):
    <code>

# Parameters are variables that you can use inside your function. 
# A function can be declared with different number of parameters. 
# In the example above, param_1 and param_2 are parameters.

# Modify your function declaration so 
# that it takes two parameters called message and offset.

# After that, 
# you'll see an error appear in the terminal. 
# You'll see how to solve it in the next steps.

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)

caesar()

# Step 54
# Inside your function body, 
# rename the text and shift variables to message and offset, 
# respectively.

text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''

    for char in message.lower():
        if char == ' ':
            encrypted_message += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    
    print('encrypted text:', encrypted_message)

caesar()

# Step 55

# Currently, your code raises a TypeError, 
# because the caesar function is defined with two parameters (message and offset), therefore it expects to be called with two arguments.

# Calling caesar() without the required arguments stops the execution of the code.

# Give message and offset values, 
# by passing text and shift as arguments to the caesar function call.

text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)

# Step 56
# At the bottom of your code, after your existing caesar(text, shift) call, call your function again.

# This time, pass the text variable and the integer 13 as arguments.

text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)
caesar(text, 13)

# Step 57
# Currently, every single letter is always encrypted with the same letter,
# depending on the specified offset. What if the offset were different for each letter?
# That would be much more difficult to decrypt. 
# This algorithm is referred to as the Vigenère cipher, 
# where the offset for each letter is determined by another text, called the key.

# Start transforming your Caesar cipher into a Vigenère cipher
# by removing the two function calls.

text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Step 58
# Now modify your function declaration: 
# change the function name into vigenere and the second parameter into key.

text = 'Hello Zaira'
shift = 3

def vigenere(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Step 59
# Delete your shift variable. 
# Then, declare a new variable called custom_key and assign the value of the string 'python' to this variable.

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Step 60
# Since your key is shorter than the text that you will have to encrypt, 
# you will need to repeat it to generate the whole encrypted text. 
# At the beginning of your function body, declare a key_index variable and set it to zero.

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Step 61
# When coding, readability is key. 
# Comments serve as effective notes, explaining the logic behind your code. 
# They prove valuable when returning to a project after some time and also aid your colleagues in understanding the code.

# In Python, you can write a comment using a #. 
# Anything that comes after the # won't be executed.

# Before your if statement, 
# add a comment saying Append space to the message.

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

# Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Step 62
# Next, inside the else block, 
# declare a variable called key_char and 
# assign it the value of key at the index key_index mod(%) the length of key.

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

    # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            key_char = key[key_index % len(key)]
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

    
# Step 63
# You will need to increase the key_index count for the next iteration. 
# To do this, after the line you just added and in the same code block, 
# use the addition assignment operator to increment key_index by one.

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Step 64
# Inside the else clause, 
# write a comment saying Find the right key character to encode.

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
        # Find the right key character to encode 
            key_char = key[key_index % len(key)]
            key_index += 1
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Step 65
# The .index() method is identical to the .find() 
# method but it throws a ValueError 
# exception if it is unable to find the substring.

# A ValueError is a built-in exception that is 
# raised when an argument with the right 
# type but inappropriate value is passed to a function.

# After incrementing key_index, 
# declare a variable named offset. 
# Find the index that key_char has in alphabet and assign it to offset. 
# Use the .index() to find the index.

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
    else:
        # Find the right key character to encode
        key_char = key[key_index % len(key)]
        key_index += 1

        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset) % len(alphabet)
        encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Step 66
# Above the offset variable, 
# create another comment saying Define the offset and the encrypted letter
text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter            
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

    
