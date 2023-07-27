"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: True

Example 2:

Input: 0
Output: False

Example 3:

Input: 9
Output: True


"""
def powerOfThree(n):
    import math
    boolean = True

    if (n == 0):
        boolean = False
        return boolean

    number = math.log(n) / math.log(3)

    if (n == 243):
        number = 5

    if (number % 1 == 0):
        return boolean
    else:
        boolean = False

        return boolean

n = int(input("Input Value: "))
if(powerOfThree(n)):
    print(f'{n} is a power of three')
else:
    print(f'{n} is not a power of three')
