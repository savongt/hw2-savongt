
### you will need this function later in the homework
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!;*:[]-+/&—")

print("== part 3 ==")
### part 3: fieldType() function
# In hw2feed.txt, note that there are both posts and comments in this feed. There are also posters.
# These lines each start with post:, reply:, and from: respectively.
# You are probably thinking "it would be really helpful if we had a function that I could
# use to figure out which type of content a line contains."
#
# The good news is that now you will write that function. 
#
# We have included some starter code to define a function fieldType(). This function should take a line as
# parameter and return the field type (either post, reply, or from).

def fieldType(line):
    # fill in your code here

# You can uncomment and test your function with these lines
#print(fieldType("from: Sean"))
#print(fieldType("post: Hi everyone"))
#print(fieldType("reply: Thanks!"))

print("== part 4 ==")
# Find out and print how many posts there are
# as well as how many comments there are
# 
# Print them as:
# Total posts: <number>
# Total replies: <number>
#

posts = 0
replies = 0

fname = "hw2feed.txt"
f = open(fname,'r',encoding='utf-8')

# Fill in your code here.

print("Total posts: %d"%posts)
print("Total replies: %d"%replies)

print("== part 5 ==")
### part 5: printing users

# Your job is to extract the names of people who made each post: and print them out,
# exactly as it is shown in the readme. 
#
# Note: only include people who made posts, not comments
# 
# Hint: if you  want to remove "from:" you can use string slicing operations
# or the replace method.
#
# You may use the fieldType() function but you do not have to. You may also define
# another function, such as fieldContents(), to help you but that is optional. 
#
# Duplicate names are expected for this part!

fname = "hw2feed.txt"
f = open(fname,'r',encoding='utf-8')
#fill in code here


print("== part 6 ==")
### part 6: counting poster contribution frequency
### Your next task in `hw2-feedprocessor.py` is to count how often each user posts or replies to the channel. 
### You will need to use a dictionary to keep a running count of how many times each user posted or replied
### (a combined count for each) to the channel:
###
### 1) The starter code begins by creating an empty dictionary, called pr_count.
###   Note that you will need to open the file again, because looping through its lines in Part 5 will
###   have "consumed" those lines. 
###
### 2) Once you’ve extracted a user name (the same thing that you printed out in part 4), think of it as a
###    key in the dictionary, whose value is the number of posts encountered by that user so far. If the key
###    is not in the dictionary, set the value to 1. If the key is already in the dictionary, set its value 
###    to 1 more than its current value. (In the language of the accumulation pattern, the count is our 
###    accumulator variable for that user.) Hint: You have to handle when you have not seen that user before.
###    You can do that with either `.get()` or with if/else statements. This is your choice.
### 
###	Once your program finishes reading through the file, print how many times each user posted or replied.
### To do this, create a string of the form: `<name>: <X>`, where <name> is the user’s name, and X is the
### number of times they posted. (See example in README.md for what it should look like.). Print that string.

pr_count = {}
f = open(fname,'r',encoding='utf-8')

# read in and count the total number of posts and replies for each user

#fill in code here


# print the number of times each user posted and replied

#fill in code here


# part 6 - How many unique posters/commenters were there?
# (hint: it's one line of code now that you have pr_count)

print("== part 7 ==")
### part 7: counting word frequency
# This is similar to post count in part 6 and you might
# even re-use some of your code. Count the number of
# times each word appears in all posts, but *not* replies
#
# use the stripWordPunctuation() function to get rid of punctuation.
# note that it is not perfect so some extra punctuation may remain.
#
# you should also convert all words to lowercase when counting.
# I.e., "the" and "The" should be the same word

postWordCount = {}
f = open(fname,'r',encoding='utf-8')

# read in and count of times each word appeared

#fill in code here


# print the number of times each word appeared, but only if the word
# appeared at least five times

#fill in code here


print("== part 8 ==")
### part 8: counting word frequency in replies and posts
# for this part, write a function, wordFreq() that will return
# the word frequency in either posts or replies as a dictionary

# This function must must take a file name and the field type
# (either post or reply) as parameters

# For example, if I want to get a dictionary of word counts in
# the posts in hw2feed.txt, I should be able to call:
# wordFreq('hw2feed.txt','post')

# You can use your code from part 7 as a starting point, or
# if you wrote part 7 using a function, you may edit it
# to meet the requirements for this part.

# uncomment and begin editing from the next line:
#def wordFreq

# to test ,you can uncomment and run these lines:
#wfp = wordFreq(fname,'post')
#if wfp["environment"] == 1 and wfp["file"] == 3 and wfp["pycharm"] == 1 and wfp.get("post",0) == 0:
#    print("Looks like wordFreq() works fine for posts")
#else:
#    print("We got some errors with wordFreq() for posts.")
# 
#wfr = wordFreq(fname,'reply') 
#if wfr["christina’s"] == 1 and wfr["be"] == 5 and wfr.get("reply",0) == 0:
#    print("Looks like wordFreq() works fine for replies")
#else:
#    print("We got some errors with wordFreq() for replies.")

