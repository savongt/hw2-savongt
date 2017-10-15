### part 1: exercises
dinocount = {'triceratops': 2, 'tyrannosaurus rex': 1, 'dilophosaurus': 2, 'parasaurolophus': 4, 'gallimimus': 12}

print("== 1 ==")
# 1: accessing values at a specified key in a dictionary.

# Write code to print the number of gallimimuses (gallimimi?) in the our dinosaur zoo (the value
# associated with key 'gallimimus' in the dictionary dinocount). Hint: this is just
# one simple line of code.
print(dinocount.get("gallimimus"))
print("== 2 ==")
# 2: incrementing the value of a dictionary at a key.
# Write code to increment the number of triceratops in the store by one (nature
# always finds a way). In other words, add 1 to the existing value of dinocount at
# key 'triceratops').  Then, print out the number of triceratops in the zoo.
dinocount["triceratops"] += 1
print(dinocount.get("triceratops"))

print("== 3 ==")
# 3: adding an entry to a dictionary. 

# Our HCDE 310 dinosaur zoo just got in a shipment of velociraptors.
# (What could go wrong?)
# 
# Write code to insert a new key, 'velociraptor' into the dictionary, with a value of 4.
# Verify that it worked by printing out the value associated with the key 'velociraptor'
dinocount["velociraptor"] = 4
print(dinocount.get("velociraptor"))

print("== 4 ==")
# 4: concatenating strings and integers. 

# Write code that creates a string that says 'Parasaurolophus: X', where X is the
# number of parasaurolophus extracted from the dinocount dictionary.  Print the string.
# Hint: you will need to use the + string concatenation operator in conjunction
# with str() or another string formatting instruction.
print("Parasaurolophus:" + str(dinocount.get("parasaurolophus")))
print("== 5 ==")
# 5: iterating over keys in a dictionary.  
for key in dinocount:
    print(key)
# Write code that prints each kind of dinosaur (key),
# one line at a time using a for loop.

print("== 6 ==")
# 6: iterating over keys to access values in a dictionary. 
for key in dinocount:
    print(key + ": " + str(dinocount.get("parasaurolophus")))
# Write code that prints each kind of dinosaur (key), followed by a colon and the
# number of that kind of dinosaur (e.g., parasaurolophus: 3), one line at a time using a for loop.

print("== 7 ==")
# 7: testing membership in a dictionary.

# Write code to test whether 'velociraptor' is in the dinocount dictionary.  If the test
# yields true, print "velociraptor: <x>", where <x> is the current number of
# velociraptors in the zoo. 
# If the test yields false, it should print "Sorry, no velociraptor in the zoo."
# Do the same thing for the key 'stegosaurus'.
if "velociraptor" in dinocount:
    print("velociraptor: " + str(dinocount.get("velociraptor")) + ", where " + str(dinocount.get("velociraptor")) + " is the current number of velociraptors in the zoo.")
else:
    print("Sorry, no velociraptor in the zoo.")
if "stegosaurus" in dinocount:
    print("stegosaurus: " + str(dinocount.get("stegosaurus")) + ", where " + str(dinocount.get("stegosaurus")) + " is the current number of stegosaurus in the zoo.")
else:
    print("Sorry, no stegosaurus in the zoo.")

print("== 8 ==")
# 8: default values

# We have a list of potential dinosaurs (in the list potentialdinosaurs)
# and we want to check whether the dinosaur exists within the zoo (dictionary).
# If it is, we want to print "dinosaur: #", where dinosaur is the 
# dinosaur name and # is the number. If the dinosaur is not in the zoo, it should
# print zero. 
# Hint: you can use default values here to make this take less code!

potentialdinosaurs = ['velociraptor','tyrannosaurus rex','brachiosaurus','archaeopteryx','gallimimus']

# put your code here
for key in potentialdinosaurs:
    if key in dinocount:
        print(key + ": " + str(dinocount.get(key)))
    else:
        print(key + ": 0")
    
print('=== 9 ===')
# 9: printing comma separated data from a dictionary.
# You may have worked with comma separated values before: they are basically 
# spreadsheets or tables represented as plain text files, with each row
# represented on a new line and each cell divided by a comma.
#
# Print out the keys and values of the dictionary stored in dinocount. The keys
# and values you print should be separated only by commas (there should be no
# spaces). Print each key,value pair on a different line. Your output should
# match the screenshot in the PDF document, although the order of the keys may
# differ.
#
# Hint: this is almost identical to exercise 6
#
# put your code here

for key in dinocount:
    print(key + ", " + str(dinocount.get(key)))

print('=== 10 ===')
# 10: saving a dictionary to a CSV file
# Write key and value pairs from dinocount out to a file named 'dinocise.csv'.
# (hint: the procedure is very close to that of (9)
#
# You should also include a header to row describe each column, labeling them as 
# "type" and "count"
#
# put your code here
import csv
with open('hw2.csv', 'w') as f:
    w = csv.DictWriter(f, dinocount.keys())
    f.write('count, type\n')
    for key in dinocount:
        f.write(key + ", " + str(dinocount.get(key)) + ", \n")

