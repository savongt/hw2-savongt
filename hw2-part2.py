###############################################################
## part 2: exercises

print('=== 1 ===')
# 1: function with one parameter
#### printAsQuestion() prints a string with a question mark (?) at the end
# input parameter:
#   s: the string to print
#
#
# to help you understand the format of instructions for these exercises, we have
# given you a starter template below. Modify it. Note how the instructions
# mention a parameter, s, which becomes the parameter name in the function
# definition.

def printAsQuestion(s):
    print(s + '?')


# uncomment the next two lines to check if you correctly defined printAsQuestion():
printAsQuestion('a word')
printAsQuestion('nice job')

print("=== 2 ===")
# 2: returning a value
#### questionString() returns a string with a question mark added to the end
# input parameter:
#   s: the string to question
# returns: a string

def questionString(s):
    return s + '?'

# uncomment the next two lines of code to check if you correctly defined the function
print(questionString('progress'))
print(questionString(questionString('nicer job')))

print("=== 3 ===")
# 3: function with two parameters that returns a value
#### charsAfter() returns a substring beginning at the specified position,
#chopping off all the characters before start_position
# input parameters:
#   start_position: index of first character to include
#   s: the string to take a slice of

def charsAfter(start_position, s):
    return s[start_position:]


# uncomment the following two lines of code to check if you correctly defined the function
#try it with different values for X and Y
X = 6
Y = 4
print(charsAfter(Y, 'not fun'))
print(charsAfter(X, 'from: John Frens'))