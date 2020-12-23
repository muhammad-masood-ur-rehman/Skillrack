Count of Power of X
Count of Power of X: N positive values v(i) where i = 1 to N are passed as input to the program. The program must print the count C of the integer values which are powers of X.
Boundary Condition(s):
1 <= N <= 10^6
1 <= v(i) <= 10^18
Input Format:
The first line contains N and X separated by a space.
The second line contains N values separated by space.
Output Format:
The first line contains C
Example Input/Output 1:
Input:
9 5
25 15 125 35 625 380625 152587890625 10 90
Output:
4
Example Input/Output 2:
Input:
7 2
1 2 4 8 16 20 32
Output:
6
def p(x,i):
    if x==1:return i==1 
    p=1 
    while(p<i):p=p*x 
    return p==i 
a,x=map(int,input().split())
y=list(map(int,input().split()));c=0
for i in y:
    if p(x,i):c+=1
print(c)
