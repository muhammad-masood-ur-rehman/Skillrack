Product of Three Integers
Given three integers A, B and C as input, the program must print the product of the three integers.
Boundary Condition(s):
0 <= A, B, C <= 999999
Input Format:
The first line contains the value of A, B and C separated by space(s).
Output Format:
The first line contains the product of the three integers.
Example Input/Output 1:
Input:
1 2 3
Output:
6
Example Input/Output 2:
Input:
1 11 10
Output:
110
a,b,c=map(int,input().split())
print(a*b*c)
