Palindrome or symmetry
Given a set of ‘n’ strings, write an algorithm and the subsequent Python code to check if the string is a Palindrome string  or Symmetry string.  A string is  said to be a palindrome string  if one half of the string is the reverse of the other half. If the length of string is odd then ignore middle character. For example, strings liril, abba are palindromes.A string is said  to be a symmetry string if both the halves of the string are same. If the length of string is odd then ignore middle character. For example, strings khokho, abab are symmetr. If the string is palindrome then print ‘Palindrome’, if the string is a symmetry string then print ‘Symmetry’ if the string (aaa) has both property then print ‘Both property’ and print ‘No property’ otherwise. Write functions to check ‘Palindrome’ and ‘Symmetry’. Make the comparisons to be case insensitive.
Input for the problem
A number and that many number of strings
Output for the problem
Whether string is Palindrome or Symmetric or both or none
from math import floor
def palindrome(text):
    if text == (text.rstrip()[::-1]):
        return True
    else:
        return False

def symmetry(text):
    n = len(text)
    if n%2:
        for i in range(n//2):
            if text[i] != text[(n//2)+1+i]:
                return False
        return True
    else:
        for i in range(n//2):
            if text[i] != text[(n//2)+i]:
                return False
        return True

n = int(input())
for i in range(n):
    text = input().rstrip().lower()
    if palindrome(text) and symmetry(text):
        print('Both property')
    elif palindrome(text):
        print('Palindrome')
    elif symmetry(text):
        print('Symmetry')
    else:

        print('No property')
