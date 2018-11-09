# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.


def measure_udacity(stringList):
    uCounter = 0
    for word in stringList:
        i = 0
        for letter in word:
            if word[i] == 'U':
                uCounter += 1
            i+= 1
    return uCounter

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2
