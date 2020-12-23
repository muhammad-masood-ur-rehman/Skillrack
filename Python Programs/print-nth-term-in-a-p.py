Print Nth term in A.P
The first two terms (a1, a2) of a strictly increasing arithmetic progression (A.P) are passed as input. The program must print the Nth term (aN) in the arithmetic progression.
Input Format:
- The first line will contain the value of the first term a1
- The second line will contain the value of the second term a2
- The third line will contain the value of N.

Boundary Conditions:
-999999 <= a1 <= 999999
-999999 <= a2 <= 999999
3 <= N <= 1000
Output Format:
The Nth term (aN) in the arithmetic progression

Example Input/Output 1:
Input:
3
6
4
Output:
12
Explanation:
The arithmetic progression is 3, 6, 9, 12, 15, ...
So the fourth term is 12
Example Input/Output 2:
Input:
-200
-20
5
Output:
520
Explanation:
The arithmetic progression is -200, -20, 160, 340, 520...
So the 5th term is 520
a1=int(input())
a2=int(input())
n=int(input())
d=a2-a1
an=a1+(n-1)*d
print(an)
