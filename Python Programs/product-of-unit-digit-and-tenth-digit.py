Product of Unit digit and Tenth digit
Product of Unit digit and Tenth digit: Given a number N where N >= 10, the program must print the product of the unit and tenth digit.
Boundary Condition(s):
10 <= N <= 9999
Input Format:
The first line contains the value of N.
Output Format:
The first line contains the product of unit digit and tenth digit in N.
Example Input/Output 1:
Input:
10
Output:
0
Example Input/Output 2:
Input:
3095
Output:
45
n=int(input())
u=int(n%10)
r=int(n%100)
t=int(r/10)
print(u*t)
