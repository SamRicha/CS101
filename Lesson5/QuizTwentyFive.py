# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    counter = 0
    result = 1
    while counter < n:
        result = result * (n - counter)
        counter = counter + 1
    return result


print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

