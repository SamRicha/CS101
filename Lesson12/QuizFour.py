# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    i = 0
    max = 0;
    for number in list_of_numbers:
        if list_of_numbers[i] > max or i == 0:
            max = list_of_numbers[i]
        i += 1
    return max

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
