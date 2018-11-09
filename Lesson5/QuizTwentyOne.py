# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


def biggest(intOne,intTwo,intThree):
    if intOne >= intTwo and intOne >= intThree:
        return intOne
    elif intTwo >= intOne and intTwo >= intThree:
        return intTwo
    elif intThree >= intOne and intThree >= intTwo:
        return intThree


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9
