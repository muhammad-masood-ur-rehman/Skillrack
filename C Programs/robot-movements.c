Robot Movements
Robot Movements: A robot movement in a R*C matrix (R rows and C columns) filled with asterisks is recorded using the following characters.
   - indicates left or right movement
   | indicates up or down movement
The program must print the number of times the robot moved left, right, up and down. The robot will not visit the same cell twice. The robot always starts from the top left cell of the matrix and ends at the bottom right cell. The input will be in the format so that more than one movement will not be possible from a given cell.
Boundary Condition(s):
2 <= R, C <= 50
Input Format:
The first line contains R and C separated a space.
The next R lines contain C characters each separated by a space.
Output Format:
The first line contains the count of left, right, up and down.
 
Example Input/Output 1:
Input:
5 6
- - | * * *
| - - * - |
- - - - | |
* * * * * |
* * * * * *
 
Output:
2 7 1 5
 
Explanation:
Initially L:0 R:0 U:0 D:0.
From top left cell (0,0), the robot moves to right (0,0). L:0 R:1 U:0 D:0
Then again it moves right (0,1). L:0 R:2 U:0 D:0
Then down (0,2). L:0 R:2 U:0 D:1
Then left (1,2). L:1 R:2 U:0 D:1
Now again left (1,1).  L:2 R:2 U:0 D:1
Now down (1,0). L:2 R:2 U:0 D:2
Now right (2,0). L:2 R:3 U:0 D:2
Now right (2,1). L:2 R:4 U:0 D:2
Now right (2,2). L:2 R:5 U:0 D:2
Now right (2,3). L:2 R:6 U:0 D:2
Then up (2,4). L:2 R:6 U:1 D:2
Then right (1,4). L:2 R:7 U:1 D:2
Then down (1,5). L:2 R:7 U:1 D:3
Then again down (2,5). L:2 R:7 U:1 D:4
Then again down (3,5). L:2 R:7 U:1 D:5
Now the robot has reached bottom right.
Example Input/Output 2:
Input:
3 4
- | * *
| - * *
- - - *
 
Output:
1 4 0 2
#include<stdio.h>
#include <stdlib.h>
int left=0,right=0,up=0,down=0;

void fun(int r,int c,char arr[r][c],int i,int j,int L,int R,int U,int D)
{
    if(i==r-1 && j==c-1){
        left=L;
        right=R;
        up=U;
        down=D;
        return;
    }
    if(i<0 || j<0 || i>=r || j>=c || arr[i][j]=='*')return;
    if(arr[i][j]=='|'){
        arr[i][j]='*';
        fun(r,c,arr,i-1,j,L,R,U+1,D);
        fun(r,c,arr,i+1,j,L,R,U,D+1);
        arr[i][j]='|';
    }
    else if(arr[i][j]=='-'){
        arr[i][j]='*';
        fun(r,c,arr,i,j-1,L+1,R,U,D);
        fun(r,c,arr,i,j+1,L,R+1,U,D);
        arr[i][j]='-';
    }
    return;
}
int main()
{
    int r,c;
    scanf("%d %d\n",&r,&c);
    char arr[r][c];
    
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            scanf("%c ",&arr[i][j]);
        }
    }
    fun(r,c,arr,0,0,0,0,0,0);
    printf("%d %d %d %d",left,right,up,down);
    return 0;
}
