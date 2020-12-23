Product of Matrix and it's Transpose Program In Python
The program must accept two positive integers M and N as the input. The program must generate a 4x4 integer matrix by using the following conditions,
- The first element of the matrix must be the value of M.
- The successive elements are obtained by adding N to the current element.
Finally, the program must print the product of the generated matrix and it's transpose.
Note:  For the matrix product, the elements in the same positions are multiplied to get the resultant matrix.
Boundary Condition(s):
1 <= M, N <= 100
Input Format:
The first line contains the values of M and N separated by a space.
Output Format:
The first four lines contain four integers in the product of the generated matrix and it's transpose.
Example Input/Output 1:
Input:
4 1
Output:
16 40 72 112
40 81 130 187
72 130 196 270
112 187 270 361
Explanation:
The generated matrix as per the conditions mentioned above is
4 5 6 7
8 9 10 11
12 13 14 15
16 17 18 19
The transpose of the generated matrix is
4 8 12 16
5 9 13 17
6 10 14 18
7 11 15 19
The product of the generated matrix and it's transpose is
16 40 72 112
40 81 130 187
72 130 196 270
112 187 270 361
Example Input/Output 2:
Input:
3 5
Output:
9 184 559 1134
184 784 1584 2584
559 1584 2809 4234
1134 2584 4234 6084
m,n=map(int,input().split())
k=m;p=[]
for i in range(4):
    l=[]
    for j in range(4):
        l.append(k);k+=n 
    p.append(l)
a=p
r=[[0 for i in range(4)] for j in range(4)]
for i in range(4):
    for j in range(4):
        r[j][i]=a[i][j]
for i in range(4):
    for j in range(4):
        print(r[i][j]*p[i][j],end=' ')
    print()
n,m=map(int,input().split())
l=[];t=n
for j in range(4):
    p=[]
    for i in range(4):
        p.append(t)
        t+=m
    l.append(p)
tra = zip(*l)
k=0
for i in tra:
    for j in range(len(i)):
        print(i[j]*l[k][j],end=' ')
    print()
    k+=1
n,m=map(int,input().split())
y=[];f=[];l=[];t=n 
for j in range(4):
    p=[]
    for i in range(4):p.append(t):
        t+=m
    l.append(p)
trans=zip(*l)
for i in trans:
    y=[]
    for j in i:y.append(j)
    f.append(y)
for i in range(4):
    for j in range(4):
        print(f[i][j]*l[i][j],end=' ')
    print()
