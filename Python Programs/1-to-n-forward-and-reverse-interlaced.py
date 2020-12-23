1 to N - Forward and Reverse Interlaced
The program must accept a number N and print the numbers from 1 to N in both forward and reverse direction interlaced with each other
INPUT FORMAT:
The first line contains N
OUTPUT FORMAT:
The first line contains the values from 1 to N in both forward and reverse direction interlaced with each other
EXAMPLE INPUT/OUTPUT:
Input
9
Output
1 9 2 8 3 7 4 6 5 5 6 4 7 3 8 2 9 1
n=int(input())
c=list()
for i in range(1,n+1):
    c.append(i)
b=list(c[::-1])  
for l in range(n):
    print(c[l],end=' ')
    print(b[l],end=' ')
