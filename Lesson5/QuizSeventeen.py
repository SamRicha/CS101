# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.


def bigger(num1,num2):
    if num1 >= num2:
        return num1
    elif num2 >= num1:
        return num2
    


print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3
