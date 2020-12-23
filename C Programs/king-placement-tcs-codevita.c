King Placement - TCS CodeVita
King Placement - TCS CodeVita: This is a typical chess game where your opponent first places a random number of Knights, Rooks, Bishops and Queens on an NxN chessboard and then you have to place your king safely on the chessboard such that it should not be under attack by any piece.
The program must accept an integer N representing the size of a chessboard and the indices of K Knights, R Rooks, B Bishops and Q Queens as the input. The program must print the number of squares on the chessboard such that your King is not attacked by any of your opponent's pieces.
Note:
The Knight moves two squares horizontally or vertically and then one more square at a right-angle.
The Rook moves in a straight line either horizontally or vertically.
The Bishop moves in a straight line diagonally on the board.
The Queen moves in a straight line either vertically, horizontally or diagonally.
Boundary Condition(s):
2 <= N <= 50
0 <= K + R + B + Q <= N*N
0 <= Indices of each piece <= N-1
Input Format:
The first line contains N.
The next line contains K, number of Knights. The next K lines, each contains two integers denoting the indices of the Knights.
The next line contains R, number of Rooks. The next R lines, each contains two integers denoting the indices of the Rooks.
The next line contains B, number of Bishops. The next B lines, each contains two integers denoting the indices of the Bishops.
The next line contains Q, number of Queens. The next Q lines, each contains two integers denoting the indices of the Queens.
Output Format:
The first line contains an integer representing the number of squares where King can be placed safely.
Example Input/Output 1:
Input:
4
2
0 0
1 1
1
2 2
0
1
3 3
Output:
2
Explanation:
The 4x4 chessboard with 2 Knights, 1 Rook and 1 Queen is given below.
K * * *
* K * *
* * R *
* * * Q
Each asterisk in the above chessboard indicates an empty square.
There are two squares to keep the king safe. i.e., (0, 1) and (1, 0).
K S * *
S K * *
* * R *
* * * Q
S indicates a safe position to place the King.
Example Input/Output 2:
Input:
8
4
2 6
3 2
5 6
7 7
4
2 2
4 6
6 4
7 5
4
0 4
1 1
1 6
5 1
2
3 5
6 0
Output
5
Explanation:
The 8x8 chessboard with 4 Knights, 4 Rooks, 4 Bishops and 2 Queens is given below.
* * * * B * * *
* B * * * * B *
* * R * * * K *
* * K * * Q * *
* * * * * * R *
* B * * * * K *
Q * * * R * * *
* * * * * R * K
Each asterisk in the above chessboard indicates an empty square.
There are five squares to keep the king safe. i.e., (0, 1), (0, 3), (1, 7), (3, 1) and (5, 7).
* S * S B * * *
* B * * * * B S
* * R * * * K *
* S K * * Q * *
* * * * * * R *
* B * * * * K S
Q * * * R * * *
* * * * * R * K
S indicates a safe position to place the King.
Example Input/Output 3:
Input:
3
1
0 2
1
0 0
2
2 2
1 0
0
Output:
2
void R(int r,int c,char a[r][c],int i,int j){
    int i1=i+1,j1=j;
    while((a[i1][j1]=='*'||a[i1][j1]=='0')&&i1<r)
    a[i1++][j1]='0';
    i1=i-1;
    while((a[i1][j1]=='*'||a[i1][j1]=='0')&&i1>=0)
    a[i1--][j1]='0';
    i1=i;j1=j+1;
    while((a[i1][j1]=='*'||a[i1][j1]=='0')&&j1<c)
    a[i1][j1++]='0';
    j1=j-1;
    while((a[i1][j1]=='*'||a[i1][j1]=='0')&&j1>=0)
    a[i1][j1--]='0';
}
void B(int r,int c,char a[r][c],int i,int j){
    int i1=i+1,j1=j+1;
    while((a[i1][j1]=='*'||a[i1][j1]=='0')&&(i1<r&&j1<c))
    a[i1++][j1++]='0';
    i1=i+1;j1=j-1;
    while((a[i1][j1]=='*'||a[i1][j1]=='0')&&(i1<r&&j1>=0))
    a[i1++][j1--]='0';
    i1=i-1;j1=j-1;
    while((a[i1][j1]=='*'||a[i1][j1]=='0')&&(i1>=0&&j1>=0))
    a[i1--][j1--]='0';
    i1=i-1;j1=j+1;
    while((a[i1][j1]=='*'||a[i1][j1]=='0')&&(i1>=0&&j1<c))
    a[i1--][j1++]='0';
}
void Q(int r,int c,char a[r][c],int i,int j){
    R(r,c,a,i,j);
    B(r,c,a,i,j);
}
void K(int r,int c,char a[r][c],int i,int j){
    if(a[i+2][j+1]=='*'&&i+2<r&&j+1<c)
    a[i+2][j+1]='0';
    if(a[i+2][j-1]=='*'&&i+2<r&&j-1>=0)
    a[i+2][j-1]='0';
    if(a[i-2][j+1]=='*'&&i-2>=0&&j+1<c)
    a[i-2][j+1]='0';
    if(a[i-2][j-1]=='*'&&i-2>=0&&j-1>=0)
    a[i-2][j-1]='0';
    if(a[i+1][j+2]=='*'&&i+1<r&&j+2<c)
    a[i+1][j+2]='0';
    if(a[i-1][j+2]=='*'&&i-1>=0&&j+2<c)
    a[i-1][j+2]='0';
    if(a[i+1][j-2]=='*'&&i+1<r&&j-2>=0)
    a[i+1][j-2]='0';
    if(a[i-1][j-2]=='*'&&i-1>=0&&j-2>=0)
    a[i-1][j-2]='0';
}
#include <stdio.h>
int main(){
    int n,k,x,y,c=0;
    scanf("%d",&n);
    char a[n][n],b[4]={'K','R','B','Q'};
    memset(a, '*', n*n);
    for(int i=0;i<4;i++){
        scanf("%d",&k);
        for(int j=0;j<k;j++){
            scanf("%d %d",&x,&y);
            a[x][y]=b[i];
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(a[i][j]=='K')
            K(n,n,a,i,j);
            if(a[i][j]=='B')
            B(n,n,a,i,j);
            if(a[i][j]=='Q')
            Q(n,n,a,i,j);
            if(a[i][j]=='R')
            R(n,n,a,i,j);
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(a[i][j]=='*')
            c++;
        }
    }
    printf("%d",c);
}
