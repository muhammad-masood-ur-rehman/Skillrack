Sum of Last X Digits
Given two integers N and X as input, the program must print the sum of last X digits in the given integer N.
Boundary Condition(s):
1 <= N <= 999999999999999
1 <= X <= 15
Input Format:
The first line contains the value of N.
The second line contains the value of X.
Output Format:
The first line contains the sum of last X digits in the given integer N.
Example Input/Output 1:
Input:
28634
3
Output:
13
Example Input/Output 2:
Input:
147173
2
Output:
10
n=input().strip()
s=[]
d=int(input())
n=n[len(n)-d:]
for i in n:
    s.append(int(i))
print(sum(s))
