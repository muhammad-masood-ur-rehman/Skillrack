Alphabet for Digit
Alphabet for Digit: Given an integer N as input, the program must print the lower case alphabets (from a to i) in the position of the digits (from 1 to 9) in the given integer.
Boundary Condition(s):
1 <= N <= 9999999999999999999 
Input Format:
The first line contains the value of N.
Output Format:
The first line contains the alphabets in the position of the digits in N.
Example Input/Output 1:
Input:
456
Output:
def
Example Input/Output 2:
Input:
987
Output:
ihg
def reverse(n):
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
s="/abcdefghi"
n=reverse(n)
while n>0:
    print(s[n%10],end="")
    n=n//10
