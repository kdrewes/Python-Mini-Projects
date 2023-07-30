
# Dictionary which contains permissions
permissions = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}

n = int(input('\nInput number of files contained in filesystem: '))

# Declare dictionary which contains file name as key and permissions as values
system = dict()

print('\nInput file name followed by operations seperated by spaces: ')
for i in range(n):

    # Prompt user to input file name followed by abbreviation of permission
    commands = input(f'{i+1}) ').split()

    # Assign file name to the key and permissions as the values
    system[commands[0]] = commands[1:]

m = int(input('\nInput number of operations to the files: '))

# Declare list which collects the result of each output
collectResult = []

print('\nInput operation followed by file name: ')
for i in range(m):
    try:
        commands = input(f'{i+1}) ').split()

        abbreviation = permissions[commands[0]]

        if abbreviation in system[commands[1]]:
            collectResult.append('Ok')
        else:
            collectResult.append('Access denied')

    except KeyError:
        print('Access denied')

# Print final results
print('\n----- Output -----')
for i in range(len(collectResult)):
    print(collectResult[i])
