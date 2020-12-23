Diagonal Sum
A set of numbers forming a matrix N*N is passed as input. The program has to print the sum of numbers along the diagonals.
Input Format: The first line will contain the value of N. The next N lines will contain N numbers each separated by one or more spaces.
Boundary Conditions: 2 <= N <= 10 Value of a given number in the matrix is from 0 to 99999999.
Output Format: The sum of the numbers along the diagonals.
Example Input/Output 1:
Input:
3
5 6 7
8 9 1
2 3 4
Output:
27
Explanation: The sum of the numbers along the diagonal = 5+9+4+7+2 = 27. Please pay attention in not counting the overlapping number 9 (which is in the middle) twice.
Example Input/Output 2:
Input:
4
2 3 4 5
1 5 3 2
3 3 9 8
9 7 6 5
Output:
41
Explanation: The sum of the numbers along the diagonal = 2+5+9+5+5+3+3+9 = 41
n=int(input())
m=[[int(i) for i in input().split()]for j in range(n)]
s=sum(m[i][i] for i in range(n))
s1=sum(m[i][n-i-1] for i in range(n))
if n%2!=0:
    print(s+s1-m[n//2][n//2])
else:

    print(s+s1)
