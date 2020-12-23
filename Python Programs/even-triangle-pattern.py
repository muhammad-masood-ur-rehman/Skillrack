Even Triangle Pattern
Given an integer N as input, the program must print the pattern as mentioned in the Example Input/Output Section.
Boundary Condition(s):
2 <= N <= 1000
Input Format:
The first line contains the value of N.
Output Format:
The list of lines containing the pattern as shown in the Example Input/Output Section.
Example Input/Output 1:
Input:
14
Output:
X
14 X
8 10 12
0 2 4 6
Example Input/Output 2:
Input:
29
Output:
28
24 26
18 20 22
10 12 14 16
0 2 4 6 8
a=int(input())
t=a//2+1
m=t//2
l,n=[],0
while(m*(m+1)//2)>t:
    m-=1 
if m*(m+1)//2==t:
    k=m
else:
    k=m+1 
for i in range(k-1,-1,-1): 
    b=[]
    for j in range(i+1):
        if n<=a:
            b.append(str(n)) 
        else:
            b.append('X')
        n+=2
    l.append(b) 
for i in range(k-1,-1,-1): 
    print(*l[i]) 
