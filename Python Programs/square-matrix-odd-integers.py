Square Matrix - Odd Integers
The program must accept N integers and print a square matrix of size K*K with the odd integers present. In case there are not enough K*K odd integers among these N integers, then fill the remaining cells in the matrix with 1.
Boundary Condition(s):
1 <= N <= 1000
1 <= Each integer value <= 1000
1 <= K <= 50
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.
Output Format:
The first K lines, each containing K integers separated by a space.
Example Input/Output 1:
Input:
10
9 30 17 16 20 5 1 15 6 5
3
Output:
9 17 5
1 15 5
1 1 1
Explanation:
Here K = 3.
The odd integers in the given 10 integers are 9, 17, 5, 1, 15 and 5.
The number of odd integers is less than 9 (3 * 3),  so the remaining cells in the matrix are filled with the integer 1.
The square matrix is given below.
9 17 5
1 15 5
1 1 1
Example Input/Output 2:
Input:
7
18 16 9 25 23 18 17
2
Output:
9 25
23 17
num=int(input())
List1=list(map(int,input().split()))
tofind=int(input())
Matrix=[[1 for foo in range(tofind)]for ele in range(tofind)]
Row=0;Col=0
for ele in List1:
    if ele%2!=0:
        Matrix[Row][Col]=ele
        Row+=1 
        Col+=1
    if Col==tofind:
        Col=0
for ele in Matrix:
    print(*ele)
