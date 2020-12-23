Matrix - Inside Numbers Sum
A set of numbers forming a matrix N*N is passed as input. The program has to print the sum of numbers which are not along the edges.

Input Format:
The first line will contain the value of N.
The next N lines will contain N numbers each separated by one or more spaces.
Boundary Conditions:
3 <= N <= 10
Value of a given number in the matrix is from 0 to 99999999.
Output Format:
The sum of the numbers which are not along the edges.

Example Input/Output 1:
Input:
3
5 6 7
8 9 1
2 3 4
Output:
9
Explanation:
All numbers except 9 are along the edges. Hence the sum is 9 which is printed as output.

Example Input/Output 2:
Input:
4
2 3 4 5
1 5 3 2
3 3 9 8
9 7 6 5

Output:
20
Explanation:
The numbers which are not along the edges are 5,3,3,9 and their sum = 20
n=int(input());s=0
l=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
  for j in range(n):
    if i!=0 and j!=0 and j!=n-1 and i!=n-1:s+=l[i][j]
print(s)
