Print Matrix - Diagonal Zig Zag
Print Matrix - Diagonal Zig Zag: An R*C matrix is passed as the input to the program. The program must print the values in zig-zag order diagonally. (Please refer Example Input/Output section for more details).
Input Format:
The first line contains R and C separated by a space.
Next R lines contain C values separated by a space.
Output Format:
The first line contains all R*C elements in zig-zag order diagonally, with the elements separated by a space.
Boundary Conditions:
2 <= R, C <= 100
Example Input/Output 1:
Input:
3 3
1 2 3
4 5 6
7 8 9
Output:
1 2 4 7 5 3 6 8 9
Example Input/Output 2:
Input:
3 7
1 2 3 4 5 6 7
8 9 1 2 3 4 5
6 7 8 9 1 2 3
Output:
1 2 8 6 9 3 4 1 7 8 2 5 6 3 9 1 4 7 5 2 3
r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
s=[[] for i in range(r+c-1)]
for i in range(r):
    for j in range(c):
        if (i+j)%2==0:s[i+j].insert(0,m[i][j])
        else:s[i+j].append(m[i][j])
for i in s:
    for j in i:print(j,end=' ')
