﻿Football Player - Total Dribble Paths
A football coach wants his team to improve their dribbling skills. So he sets up a R * C grid, where R is the number of rows and C is the number of columns. From any given cell, a player can only dribble to the right cell or bottom cell.A player always starts from top left most cell and must end at bottom right most cell where he can collect the reward if he has dribbled according to the rules above.The program must accept R, C and print the total number of possible paths P in which a player can reach the destination.Input Format:
The first line contains R.
The second line contains C.
Output Format:
The first line contains P.
Boundary Conditions:
1 <= R, C <= 100
Example Input/Output 1:
Input:
2
3Output:
3
Example Input/Output 2:
Input:
3
3
Output:
6
Example Input/Output 3:
Input:
25
21
Output:
102758710
n,m = int(input()),int(input())
c = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    c[i][0] = 1
for j in range(m):
    c[0][j] = 1
for i in range(1,n):
    for j in range(1,m):
        c[i][j] = c[i-1][j]+c[i][j-1]
print(c[n-1][m-1])
