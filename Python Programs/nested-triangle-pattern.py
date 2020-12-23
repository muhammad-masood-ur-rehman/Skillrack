Nested Triangle Pattern
The program must accept an integer N as the input. The program must print a triangle based on the following conditions.
- The triangle contains (N+1)/2 layers. 
- The outermost layer contains the character H, the second outermost layer contains the character O. Similarly, the remaining layers contain the characters H and 0 alternatively. 
- Hash symbols (#) are printed in front of the first N-1 rows of the triangle to make the triangle more clear. 
Example Input/Output 1: 
Input: 
5

Output: 
####H 
###HOH 
##HOHOH 
#H00000H 
HHHHHHHHH 
Example Input/Output 2: 
Input: 
6

Output: 
#####H 
####HOH 
###HOHOH 
##HOHHHOH 
#HOOOOOOOH 
HHHHHHHHHHH
n=int(input())
r=(n+1)//2
mat=[];c=1
for i in range(n):
    s='#'*(n-i-1)+'H'*c
    c+=2 
    mat.append(list(s))
for l in range(1,r,2):
    for i in range(n):
        for j in range(n+i):
            if i<n-l and i>=l and (j==n-i+l-1 or j==n+i-l-1):
                mat[i][j]='O'
            elif i==n-l-1 and j<n+i-l and j>=n-i+l-1:
                mat[i][j]='O'
for i in mat:
    print(*i,sep="")
