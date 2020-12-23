Matrix Add Top Row
Matrix Add Top Row: A matrix of size R*C is given as the input to the program. The program must add the elements in the first row in each column to the elements in the below rows by equally dividing them. Then the program must print the modified matrix as the output.
Note: If the integer cannot be evenly divided then do not consider the decimal point values.
Boundary Condition(s):
1 <= R, C <= 100
Input Format:
The first line contains R and C separated by space.
The next R lines contain C integers each separated by space(s).
Output Format:
The first R lines contain the modified matrix as per the given condition.
Example Input/Output 1:
Input:
3 4
24 4 2 19
8 10 5 1
7 13 12 14
Output:
24 4 2 19
20 12 6 10
19 15 13 23
Example Input/Output 2:
Input:
4 4
21 24 13 14
22 12 23 11
11 22 16 16
20 16 11 20
Output:
21 24 13 14
29 20 27 15
18 30 20 20
27 24 15 24
a,b=map(int,input().split()) 
c=[list(map(int,input().split())) for i in range(a)] 
d=[] 
for i in range(b):
    d.append(c[0][i]) 
for i in range(a):
    x=0 
    for j in range(b):
        if(i==0):
            print(c[i][j],end=" ") 
        else:
            dd=d[x]//(a-1) 
            print(c[i][j]+dd,end=" ")  
            x+=1
    print()
