Identical Toys Distribution
Identical Toys Distribution: Given the number of T identical toys, find the number of ways W to distribute them among N children.
Input Format:
The first line will contain T and N separated by a space.
Output Format:
The first line will contain W. As W can be large, print the answer as modulo 1000000007
Boundary Conditions:
1 <= T, N <= 1000
Example Input/Output 1:
Input:
2 2
Output:
3
Explanation:
The three ways to disribute 2 toys among 2 children are (2,0) (0,2) (1,1)
from math import factorial
t,n=[int(i) for i in input().split()]
r=t+n-1
r1,r2,r3=factorial(r),factorial(t),factorial(r-t)
print((r1//(r2*r3))%1000000007)
