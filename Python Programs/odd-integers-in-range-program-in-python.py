Odd Integers In Range Program in Python
The program must accept two integers X and Y and print the odd integers between them.
Input Format:
The first line denotes the value of X.
The second line denotes the value of Y.
Output Format:
The first line contains the odd integers between X and Y separated by a space.
Boundary Conditions:
-999999 <= X <= 9999999
X < Y <= 9999999
Example Input/Output 1:
Input:
1
11
Output:
3 5 7 9
Example Input/Output 2:
Input:
24
30
Output:
25 27 29
n=int(input())
m=int(input())
for i in range(n+1,m):
    if i%2!=0:print(i,end=" ")
