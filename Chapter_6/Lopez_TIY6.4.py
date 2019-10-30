glossary = {
    'string': 'a sequence of characters',
    'variable': 'a value that can change, depending on conditions or on information passed to the program',
    'list': 'a data structure that is a changeable ordered sequence of elements',
    'tuple': 'a sequence of unchangeable objects',
    'dictionary': 'an unordered collection of data values, used to store data values like a map',
    'print': 'a function to display the output of a program',
    'sort': 'function that puts a list in alphabetical order, permanently',
    'range': 'function returning a list of integers, the sequence being defined by the arguments passed to it',
    'slice': 'a bracket notation that specifies the start and end of the section of the list you wish to use',
    'set': 'collection of unique but unordered items'
    }

count = 0

for term in glossary:
    count += 1
    print(f"{count}.) {term}: {glossary[term]}")

