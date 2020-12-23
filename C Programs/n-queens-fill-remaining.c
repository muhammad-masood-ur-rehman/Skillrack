N Queens - Fill Remaining
In a N*N square chessboard, Q queens are placed in Q continuous rows so that they do not attack each other. The program must accept the positions of the Q queens (marked by 1) and print the positions of the remaining N-Q queens in the remaining rows to be placed, so that they do not attack each other.
Note: In Chess, queen can move any direction diagonally. The queen can also move left or right along the row it is present. The queen can also move up or down along the column it is present. The movement can happen till the end of the board is reached or another piece (like Rook, Knight, Bishop, Pawn etc is encountered). But in this program only the N queens are placed and no other pieces will be present on the board. 
Boundary Condition(s):
4 <= N <= 10
2 <= Q <= N-1
Input Format:
The first line contains N.
The next N lines contain N values (0 or 1) each separated by a space.
Output Format:
The first line contains the shift in the position followed by the direction.
Example Input/Output 1:
Input:
4
0 1 0 0    
0 0 0 1     
0 0 0 0     
0 0 0 0     
Output:
0 1 0 0    
0 0 0 1     
1 0 0 0     
0 0 1 0
Explanation:
In this combination the queens do not attack each other.
Example Input/Output 2:
Input:
8
0 0 1 0 0 0 0 0  
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Output:
0 0 1 0 0 0 0 0  
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 1 0 0 0
0 1 0 0 0 0 0 0
#include<stdio.h>
#include <stdlib.h>
int n;
int mat[n][n];
int isValid(int row,int col){
    int i=row,j=col;
    if(leftUp(i,j))return 0;
    if(rightUp(i,j))return 0;
    if(leftDown(i,j))return 0;
    if(rightDown(i,j))return 0;
    if(colu(i,j))return 0;
    return 1;
}
int colu(int i,int j){
    for(i=0;i<n;++i){
        if(mat[i][j]==1)return 1;
    }
    return 0;
}
int leftUp(int i,int j){
    while(i>-1 && j>-1){
        if(mat[i][j]==1)return 1;
        i--;j--;
    }
    return 0;
}
int rightUp(int i,int j){
    while(i>-1 && j<n){
        if(mat[i][j]==1)return 1;
        i--;j++;
    }
    return 0;
}
int leftDown(int i,int j){
    while(i<n && j>-1){
        if(mat[i][j]==1)return 1;
        i++;j--;
    }
    return 0;
}
int rightDown(int i,int j){
    while(i<n && j<n){
        if(mat[i][j]==1)return 1;
        i++;j++;
    }
    return 0;
}
int fun(int row){
    if(row==n)return 1;
    
    for(int j=0;j<n;++j){
        if(mat[row][j]==1){
            return fun(row+1);
        }
    }
    for(int j=0;j<n;++j){
        if(isValid(row,j)){
            mat[row][j]=1;
            if(fun(row+1)){
                return 1;
            }
            mat[row][j]=0;
        }
    }
    return 0;
}
int main()
{
    scanf("%d",&n);
    
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j){
            scanf("%d",&mat[i][j]);
        }
    }
    
    fun(0);
    
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j){
            printf("%d ",mat[i][j]);
        }
        printf("\n");
    }
    return 0;
}
