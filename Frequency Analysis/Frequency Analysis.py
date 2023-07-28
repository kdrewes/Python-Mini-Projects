n = int(input('Input number of phrases: '))
dictionary = dict()
numberSet = set()
words = ""
wordList = []

for i in range(n):
    words += input(f'input phrase #{i+1}: ')
    words += ' '
words = words.split()

for i in words:
    if (i not in dictionary.keys()):
        dictionary[i] = words.count(i)

newDictionary = dict((value, key) for key, value in dictionary.items())

for k, v in sorted(newDictionary.items(), reverse=True):
    for dk, dv in sorted(dictionary.items()):
        if (k == dv):
            print(dk, dv, end='\n')





