N numbers divisible by X or Y
Three integers X, Y and N are passed as input. The program must print the first N values from 1 which are divisible by X or Y.
Boundary Condition(s):
1 <= X, Y, N <= 999
Input Format:
The first line contains the value of X.
The second line contains the value of Y.
The third line contains the value of N.
Output Format:
The first line contains N integers separated by a space.
Example Input/Output 1:
Input:
3
7
10
Output:
3 6 7 9 12 14 15 18 21 24

Example Input/Output 2:
Input:
4
5
8
Output:
4 5 8 10 12 15 16 20
x=int(input())
y=int(input());k=[]
n=int(input());n=abs(n);i=1
while n:
    if i%x==0 or i%y==0:k.append(i);n-=1
    i+=1
print(*k)
