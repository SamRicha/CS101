# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(word):
    if word == '': 
        return True
    else:
        if word[0] == word [-1]:
            new_word = word[1:-1]
            return is_palindrome(new_word)
        else:
            return False
 
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True
