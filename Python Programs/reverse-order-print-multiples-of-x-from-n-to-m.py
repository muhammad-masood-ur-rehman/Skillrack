Reverse Order - Print multiples of X from N to M
Two numbers M and N are passed as the input. A number X is also passed as the input. The program must print the numbers divisible by X from N to M (inclusive of M and N).
Input Format:
The first line denotes the value of M
The second line denotes the value of N
The third line denotes the value of X
Output Format:
Numbers divisible by X from N to M, with each number separated by a space.
Boundary Conditions:
1 <= M <= 9999999
M < N <= 9999999
1 <= X <= 9999
Example Input/Output 1:
Input:
2
40
7
Output:
35 28 21 14 7
Example Input/Output 2:
Input:
66
121
11
Output:
121 110 99 88 77 66
m=int(input())
n=int(input())
x=int(input())
l=[]
for i in range(m,n+1):
    if (i%x==0):
        l.append(i)
print(*l[::-1])
