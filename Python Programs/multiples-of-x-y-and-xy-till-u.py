Multiples of X, Y and X+Y Till U
Multiples of X, Y and X+Y Till U: Given two numbers X and Y and an upper limit U, print multiples of X, Y and X+Y till U (not inclusive of U) in both forward and reverse directions.
Boundary Condition:
1 <= X,Y <= 100
1 <= U <= 9999999
Input Format:
The first line contains X and Y separated by a space.
The second line contains U.
Output Format:
The first line contains the multiples of X, Y and X+Y from 1 to U in forward direction.
The second line contains the multiples of X, Y and X+Y from 1 to U in reverse direction.
Example Input/Output 1:
Input:
3 6
24
Output:
3 6 9 12 15 18 21
21 18 15 12 9 6 3
Example Input/Output 2:
Input:
4 7
45
Output:
4 7 8 11 12 14 16 20 21 22 24 28 32 33 35 36 40 42 44
44 42 40 36 35 33 32 28 24 22 21 20 16 14 12 11 8 7 4
x,y=map(int,input().split())
u=int(input())
l=[]
for i in range(min(x,y),u):
    if i%x==0 or i%y==0 or i%(x+y)==0:
        l.append(i)
print(*l)
print(*l[::-1])
