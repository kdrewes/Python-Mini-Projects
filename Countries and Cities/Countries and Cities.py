
locations = dict()

n = int(input('Input number of countries and cities: ').strip())
words = ""

print('\nInput country followed by cities in that country: ')
for i in range(n):
    words = input(f'{i+1}) ').split()
    locations[words[0]] = words[1:]

m = int(input('\nInput number of cities: ').strip())
city = ""
collection = []

for i in range(m):
    city = input(f'{i+1}) ').strip()

    for k in locations.keys():
        if city in locations[k]:
            collection.append(k)
            break

print('\n------- Output -------')
for i in range(len(collection)):
    print(collection[i])