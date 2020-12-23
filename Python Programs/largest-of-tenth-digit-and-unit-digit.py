Largest of Tenth Digit and Unit Digit
Largest of Tenth Digit and Unit Digit: Given an integer N as input, the program must print the largest of the tenth digit and  the unit digit in the integer N.
Boundary Condition(s):
10 <= N <= 9999999
Input Format:
The first line contains the N value.
Output Format:
The first line contains the largest of the tenth digit and the unit digit in the integer N.
Example Input/Output 1:
Input:
5442
Ouput:
4
Explanation :
Tenth digit (4) is greater than unit digit (2).
Example Input/Output 2:
Input:
4567
Ouput:
7
Explanation :
Unit digit (7) is greater than tenth digit (6).
n=int(input())
a=int(n%10)
b=int((n/10)%10)
if a>b:
    print(a)
else:
    print(b)
