Absolute Value of N is Power of X
Absolute Value of N is Power of X: The program accepts two integers N and X as input. The program prints YES if the absolute value of N is a power of X. Else the program prints NO.
Boundary Condition(s):
-1015 <= N <= 1015
1 <= X <= 100
Input Format:
The first line contains N and X separated by a space.
Output Format:
The first line contains YES or NO.
Example Input/Output1:
Input:
32 2
Output:
YES
Example Input/Output2:
Input:
26 3
Output:
NO
def power(b,a):
  p=1
  while(p<a):p*=b
  return p==a
a,b=map(int,input().split())
i=1
if power(abs(b),abs(a)):print('yes')
else:print('no')
