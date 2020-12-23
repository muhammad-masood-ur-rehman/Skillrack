Matrix Rotation - Anti Clock Wise
A M*N matrix having M rows and N columns containing integer values is passed as the input. The matrix must be rotated R times in counter-clock (anti-clock) wise direction and the resulting matrix must be printed as the output.
Input Format:
The first line will contain the value of M, N and R, each separated by a space. (M is the number of rows, N is the number of cols and R is the rotation count)
The next M lines will contain N integer values
Output Format:
M lines with each line containing N integer values of the rotated matrix (with each value separated by a space).
Constraints:
2 <= M <= 300
2 <= N <= 300
1 <= R <= 10^9
Values of integers in the matrix is from 1 to 10000000
Example Input/Output 1:
Input:
4 4 1
1 2 3 4
5 6 7 8
9 10 11 12
100 101 102 103
Output:
2 3 4 8
1 7 11 12
5 6 10 103
9 100 101 102
Example Input/Output 2:
Input:
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 30
Output:
30 27 26 25
22 9 15 19
16 8 21 13
10 14 20 7
4 3 2 1
def matrixRotation(matrix,r):
   m, n = len(matrix), len(matrix[0])
   b = [[None]*n for _ in range(m)]
   indices = []

   for c in range(min(m,n)//2):
       index = []
       for i in range(c,n-c): index.append((c,i))
       for i in range(c+1,m-1-c): index.append((i,n-1-c))
       for i in range(c,n-c)[::-1]: index.append((m-1-c,i))
       for i in range(1+c,m-1-c)[::-1]: index.append((i,c))
       if not index:
           break
       indices.append(index)

   rotated = []
   for index in indices:
       k = r%len(index)
       rotated.append(index[k:]+index[:k])

   for (x,y) in zip(indices,rotated):
       for ((c,d),(e,f)) in zip(x,y):
           b[c][d] = matrix[e][f]

   return b
m,n,r = map(int,input().split())
matrix = [input().split() for i in range(m)]
for i in matrixRotation(matrix,r):
   print(*i)
rows, cols, rotations = [int(x) for x in input().strip().split(" ")]
num_layers = int(min(rows, cols)/2)
layers = [[] for x in range(num_layers)]
data = []
for row in range(rows):
data.append([int(x) for x in input().strip().split(" ")])
rows -= 1
cols -= 1
for current_layer in range(num_layers):
i = j = current_layer
while i < rows-current_layer:
layers[current_layer].append(data[i][j])
i += 1
while j < cols-current_layer:
layers[current_layer].append(data[i][j])
j += 1
while i > current_layer:
layers[current_layer].append(data[i][j])
i -= 1
while j > current_layer:
layers[current_layer].append(data[i][j])
j -= 1
new_layers = []
for layer in layers:
rots = rotations%len(layer)
new_layers.append(list(layer[-rots:] + layer[:-rots]))
for current_layer in range(num_layers):
i = j = current_layer
while i < rows-current_layer:
data[i][j] = new_layers[current_layer].pop(0)
i += 1
while j < cols-current_layer:
data[i][j] = new_layers[current_layer].pop(0)
j += 1
while i > current_layer:
data[i][j] = new_layers[current_layer].pop(0)
i -= 1
while j > current_layer:
data[i][j] = new_layers[current_layer].pop(0)
j -= 1
for row in range(rows+1):
for col in range(cols+1):
print(data[row][col], end=" ")
print()
