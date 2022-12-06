'''
Dictionary list are used to story data in a key:value paring.
These list do not allow duplicates.
As of Python version 3.7, dictionaries are ordered.
In Python 3.6 and earlier, dictionaries are unordered.
'''

dict1 = {
    "make":"chevy",
    "model":"cavelier",
    "year": 1990
}
print(dict1)

# You can reference an item pairing by key name
print(dict1["year"]) # This will print the value of "year"
