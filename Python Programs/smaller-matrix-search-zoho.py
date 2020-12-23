Smaller Matrix Search [ZOHO]
Smaller Matrix Search [ZOHO]: A bigger NxN matrix is passed as the input. Also a smaller MxM matrix is passed as input. The program must print TRUE if the smaller matrix can be found in the bigger matrix. Else the program must print FALSE.
Input Format:
First line will contain the value of N.
Second line will contain the value of M.
Next N lines will contain the values in the N*N matrix with each value separated by one or more space.
Next M lines will contain the values in the M*M matrix with each value separated by one or more space.
Output Format:
First line will contain the string value TRUE or FALSE
Boundary Conditions:
3 <= N <= 20
2 <= M <= N
Example Input/Output 1:
Input:
3
2
4 5 9
1 3 5
8 2 4
3 5
2 4
Output:
TRUE
Example Input/Output 2:
Input:
3
2
4 5 9
1 3 5
8 2 4
4 5
1 4
Output:
FALSE
n=int(input());x=0;y=0
m=int(input());c=0;f=0
a=[list(map(int,input().split())) for i in range(n)]
b=[list(map(int,input().split())) for i in range(m)]
for i in range(n):
    c=0;p=0;q=0
    for j in range(n):
        if a[i][j]==b[p][q]:
            x=i;y=j
            for p in range(m):
                for q in range(m):
                    if a[x][y]==b[p][q]:y+=1;c+=1 
                x+=1;y=j
    if c==m*m:f=1;break
if f==1:print('TRUE')
else:print('FALSE')
n=int(input())
m=int(input())
N=[0] * n
for i in range(n):
    N[i]=list(map(int,input().split()))
S=[]
S=[0] * m
for i in range(m):
    S[i]=list(map(int,input().split()))
flag=0
p=0
q=0
for i in range(n):
    c=0
    p=0
    q=0
    for j in range(n):
        if N[i][j]==S[p][q]:
            x=i
            y=j
            for p in range(m):
                for q in range(m):
                    if N[x][y]==S[p][q]:
                        y=y+1
                        c=c+1
                x=x+1
                y=j
    if c==m*m:
        flag=1
        break
                
if flag==1:
    print("TRUE")
else:
    print("FALSE")
