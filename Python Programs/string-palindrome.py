String Palindrome
A string S is passed as input to the program. The program must print "yes" if the string S is a palindrome and must print "no" if the string is NOT a palindrome.
Input Format:
The first line will contain the value of the string S.
Example Input/Output 1:
Input:
malayalam
Output:
yes

Example Input/Output 2:
Input:
manager
Output:
no
def check_if_palindrome(s):
  return s == s[::-1]
s=input().strip()
if check_if_palindrome(s):
    print("yes")
else:
    print("no")
