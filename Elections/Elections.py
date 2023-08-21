number = int(input('Input Number of Votes: '))

array = []
dictionary = dict()
sum = 0
name = ""

print('\nInput candidate followed by numbers of votes:')
for i in range(0, number):
    word = input()
    n1, n2 = word.split()
    array.append([n1, n2])

print('\n------------ Results: ------------')
for i in range(0, number):
    if (array[i][0] not in dictionary):
        name = array[i][0]
        for x in range(0, number):
            if (array[x][0] == name):
                sum += int(array[x][1])
        dictionary[name] = sum
        sum = 0

for i in sorted(dictionary):
    print(i, dictionary[i], end=' ')

print()
