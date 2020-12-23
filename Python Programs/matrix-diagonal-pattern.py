Matrix Diagonal Pattern
Given an integer matrix of size N*N as input, the program must print only the diagonal elements. The remaining elements must be replaced by *
Boundary Condition(s):
1 <= N <= 50
Input Format:
The first line contains the value of N.
The next N lines contain N values separated by space(s).
Output Format:
The first N lines contain the modified matrix as mentioned above.
Example Input/Output 1:
Input:
3
1 8 9
4 8 7
5 2 8
Output:
1 * 9 
* 8 * 
5 * 8 
Example Input/Output 2:
Input:
6
31 62 5 8 39 3 
37 2 79 76 97 81 
9 1 43 86 5 37 
9 77 85 45 87 36 
41 6 65 75 9 3 
22 69 45 83 20 90
Output:
31 * * * * 3 
* 2 * * 97 * 
* * 43 86 * * 
* * 85 45 * * 
* 6 * * 9 * 
22 * * * * 90
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(l[i][j],end=" ")
        else:
            print('*',end=" ")
    print()
