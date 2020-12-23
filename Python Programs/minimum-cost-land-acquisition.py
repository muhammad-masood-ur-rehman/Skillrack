Minimum Cost - Land Acquisition
Minimum Cost - Land Acquisition: The government of India plans to build a road In a city. The government also plans to acquire some lands to start the construction. The program must accept an Integer matrix of size N*N representing the heights of the buildings (i.e., the number of storeys In each building) in the city. A positive value X in the matrix indicates that there is an X-storey building. A zero value in the matrix indicates the presence of land that cannot be acquired by the government. 
The rules for road construction In the city are given below.
- The road always starts from the first row and ends at the last row. 
- No more than one building In a row can be acquired by the government. 
The cost to acquire an X-storey building is X. The government has decided to acquire the lands with the minimum cost M. The program must print the minimum cost M to acquire land for road construction in the given city as the output. 
NOTE: It is always possible to build a road In the given city.
Input Format: 
The first line contains N. 
The next N lines, each contains N Integers separated by space. 

Output Format: 
The first line contains M.

Example Input/Output 1: 
Input: 
4 
0 0 2 0 
1 3 4 5
5 0 7 0
8 1 2 3
Output: 
11

Example Input/Output 2: 
Input: 
3
1 2 0
4 3 1
5 2 1
Output: 
4
n=int(input())
mat=[list(map(int,input().split())) for r in range(n)]
for r in range(1,n):
    for c in range(0,n):
        if mat[r][c]==0:
            continue
        building=[]
        if c!=0 and mat[r-1][c-1]!=0:
            building.append(mat[r-1][c-1])
        if c!=n-1 and mat[r-1][c+1]!=0:
            building.append(mat[r-1][c+1])
        if mat[r-1][c]!=0:
            building.append(mat[r-1][c])
        if building:
            mat[r][c]+=min(building)
        else: mat[r][c]=0
print(min([i for i in mat[n-1] if i!=0]))
