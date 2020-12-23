Numbers - First and Last Digits Same
N numbers A(1) to A(N) are passed as input. The program must print only the X numbers which have same first and last digit.

Input Format:
The first line contains N.
The second line contains N numbers separated by a space.

Output Format:
The first line contains the X numbers separated by a space.

Boundary Conditions:
2 <= N <= 200
10 <= A(i) <= 9999999
1 <= X <= N

Example Input/Output 1:
Input:
4
102 333 282 500
Output:
333 282
n=int(input())
v=[i for i in input().split()]
for i in v:
        if i[0]==i[len(i)-1]:
            print(i)
