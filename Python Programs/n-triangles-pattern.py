N Triangles Pattern
The program must accept an integer N as the input. The program must print N triangles numbered from 1 to N based on the following conditions.
- The Xth triangle contains (2*X)-1 lines.
- The 1st line contains the integer 1.
- The 2nd line contains the integers from 2 to 1.
- The 3rd line contains the integers from 3 to 1. Similarly, the first X lines of the triangle are printed.
- The (X+1)th line contains the integers from X-1 to 1.
- The (X+2)th line contains the integers from X-2 to 1.
- The (X+3)th line contains the integers from X-3 to 1. Similarly, the remaining lines of the triangle are printed.
Boundary Condition(s):
2 <= N <= 25
Input Format:
The first line contains N.
Output Format:
The first N*N lines contain the integer value(s) based on the given conditions.
Example Input/Output 1:
Input:
3
Output:
1 
1 
2 1 
1 
1 
2 1 
3 2 1 
2 1 
1 
Explanation:
Here N = 3, so 3 triangles are printed.
First Triangle:
1
Second Triangle:
1
2 1
1
Third Triangle:
1
2 1
3 2 1
2 1
1
Example Input/Output 2:
Input:
4
Output:
1
1
2 1
1
1
2 1
3 2 1
2 1
1
1
2 1
3 2 1
4 3 2 1
3 2 1
2 1
1
m=int(input())
n=1
while(n<m+1):
    for i in range(n):
        for j in range(i+1,0,-1):
            print(j,end=" ")
            j+=1 
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print(i,end=" ")
            i-=1 
        print()
    n+=1
