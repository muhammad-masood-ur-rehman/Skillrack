First and Last X Digits
First and Last X Digits: Given a number N, print the first and last X digits of the number.
Input Format:
The first line contains N.
The second line contains X.
Output Format:
The first line contains the first X digits of N.
The second line contains the last X digits of N.
Boundary Condition:
X <= Length of N <= 20
Example Input/Output 1:
Input:
123456
2
Output:
12
56
Example Input/Output 2:
Input:
00010245699
3
Output:
102
699
s=input().strip()
s=str(int(s))
d=int(input())
a=s[:d]
s=s[::-1]
b=s[:d][::-1]
print(a,b,sep='\n')
