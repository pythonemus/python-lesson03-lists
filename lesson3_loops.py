'''
This lesson we will demonstrate how to iterate the items in lists
Python does not have many of the diffent looping forms as other traditional languages
Python uses only the "for" and "while" to iterate through items in lists
'''

#We will start with the same list from form the other examples
list1 = ['red', 'blue', 'green']
dict1 = {
    "make":"chevy",
    "model":"cavelier",
    "year": 1990
}

# The "for" loop will iterate through list1 and print all the items in the list
for items in list1:
    print('color is '+items)


# This "for" loop will capture the key and value from the dictionary list
for key,val in dict1.items():
    print('this is the key: '+key)
    print('this is the value: '+str(val))
    print('this is the key:value pairing '+key+':'+str(val))

# This example of a "while" loop
# The "while" loop will remain "true" until i becomes greater than 6
i = 1
while i < 6:
   print(i)
   i += 1