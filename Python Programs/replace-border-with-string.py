Replace Border with String
The program must accept a character matrix of size RxC and a string S as the input. The program must replace the characters in the border of the matrix with the characters in the string S in the clockwise direction. Then the program must print the modified matrix as the output. 
Example Input/Output 1: 
Input: 
4 5
@ b c d E
e f 5 h i
b c d e q
k 9 o l 2 
queenbee
Output: 
q u e e n
e f 5 h b
b c d e e
k 9 o l e
Example Input/Output 2: 
Input:
3 3
A b c
d * f
g h i
d@$zling 
Output: 
d @ $
g * z 
n i l
R,C=map(int,input().split())
matrix=[list(map(str,input().split())) for ctr in range(R)]
S=input().strip()
row,col=0,0
for ch in S:
    matrix[row][col]=ch
    if row==0 and col<C-1:
        col+=1
    elif row==R-1 and col>0:
        col-=1
    elif col==C-1 and row<R-1:
        row+=1 
    elif col==0 and row>0: 
        row-=1 
for val in matrix:
    print(*val) 
