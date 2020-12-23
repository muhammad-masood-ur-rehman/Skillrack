Square Pattern Printing For N
Square Pattern Printing For N: Given N, print the pattern as described in the Example Input/Output.
Input Format:
The first line will contain N.
Output Format:
N lines will contain the required pattern.
Boundary Conditions:
1 <= N <= 50
Example Input/Output 1:
Input:
5
Output:
1 2 3 4 5
2 4 6 8 4
4 8 12 10 8
8 16 18 20 10
16 26 36 28 20
Example Input/Output 2:
Input:
4
Output:
1 2 3 4
2 4 6 3
4 8 7 6
8 11 14 7
a=int(input()) 
b=[[0 for i in range(a)]for i in range(a)] 
c=1 
for i in range(a):
    b[0][i]=c 
    c+=1   
for i in range(1,a):
    b[i][0]=b[i-1][1] 
    for j in range(1,a-1):
        b[i][j]=b[i-1][j-1]+b[i-1][j+1] 
    b[i][a-1]=b[i-1][a-2] 
for i in b:
    print(*i)
