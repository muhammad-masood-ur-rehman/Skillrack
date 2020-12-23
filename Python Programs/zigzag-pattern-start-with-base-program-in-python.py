ZigZag Pattern - Start with Base Program in Python
ZigZag Pattern - Start with Base: Two positive integer values X and Y are passed as input to the program. The program must print the output based on X and Y values as shown in the Example Input/Output section.
Boundary Condition(s):
1 <= X, Y <= 1000
Input Format:
The first line contains the value of X and Y separated by a space.
Output Format:
The X lines contain the desired pattern.
Example Input/Output 1:
Input:
5 11
Output:
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
30 29 28 27 26
31 32 33 34 35
Example Input/Output 2:
Input:
6 12
Output:
12 13 14 15 16 17
23 22 21 20 19 18
24 25 26 27 28 29
35 34 33 32 31 30
36 37 38 39 40 41
47 46 45 44 43 42
a,b=map(int,input().split())
for i in range(1,a+1):
    if i%2!=0:
        for j in range(1,a+1):print(b,end=' ');b+=1
    else:
        p=[]
        for j in range(1,a+1):p.append(b);b+=1
        print(*p[::-1],end=' ')
    print()
