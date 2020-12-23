Both Adjacent Elements - Odd or Even
Both Adjacent Elements - Odd or Even: Given an array of N positive integers, print the positive integers that have both the adjacent element values as odd or even.
Boundary Condition(s):
3 <= N <= 1000
Input Format:
The first line contains N.
The second line contains N elements separated by space(s).
Output Format:
The first line contains the elements (which have both the adjacent element values as odd or even) separated by a space.
Example Input/Output 1:
Input:
7
10 21 20 33 98 66 29
Output:
21 20 33
Example Input/Output 2:
Input:
5
11 21 30 99 52
Output:
30 99
n=int(input())
l=list(map(int,input().split()))
for i in range(1,len(l)-1):
    if( (l[i-1]%2!=0 and l[i+1]%2!=0) or (l[i-1]%2==0 and l[i+1]%2==0)):
        print(l[i],end=' ')
a=int(input());l=list(map(int,input().split()))
for i in range(1,a-1):
   if (l[i-1]%2 and l[i+1]%2) or (l[i-1]%2==0 and l[i+1]%2==0):
           print(l[i],end=' ')
