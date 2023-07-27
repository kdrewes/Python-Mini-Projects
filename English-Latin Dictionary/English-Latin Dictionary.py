
n = int(input())
words = ""
copyWords = ""
dictionary = dict()

for i in range(n):
    words += input()
    words += ' '
    for x in range(len(words)):
        if(words[x] == '-' or words[x] == ','):
            copyWords += ' '
        elif(words[x] == ' '):
            continue
        else:
            copyWords += words[x]

    words = copyWords
    words = words.split()
    dictionary[words[0]] = words[1:]
    copyWords = ""
    words = ""

latinDictionary = dict()

for k,v in dictionary.items():
    for i in range(len(v)):
        if v[i] not in latinDictionary.keys():
            latinDictionary[v[i]] = k
        else:
            latinDictionary[v[i]] += ", "
            latinDictionary[v[i]] += k

for k,v in sorted(latinDictionary.items()):
    print(k," - ", v)