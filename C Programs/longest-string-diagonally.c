Longest String - Diagonally
Longest String - Diagonally: The program must accept a character matrix of size RxC and the position of a cell (X, Y) as the input. The program must form four string values based on the following conditions.
- The string S1 must be formed by traversing the cells from the given cell diagonally in the top-left direction.
- The string S2 must be formed by traversing the cells from the given cell diagonally in the top-right direction.
- The string S3 must be formed by traversing the cells from the given cell diagonally in the bottom-right direction.
- The string S4 must be formed by traversing the cells from the given cell diagonally in the bottom-left direction.
Finally, the program must print the longest string among the four string values as the output. If two or more string values have the same maximum length, the program  must print the first occurring string as the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= X <= R
1 <= Y <= C
Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The (R+2)nd line contains X and Y separated by a space.
Output Format:
The first line contains the longest string among the four string values.
Example Input/Output 1:
Input:
6 8
D y j w h r y t
s a r A v g t y
l E b v m B y F
F p z w E j n s
m f p D j d r y
D v w r s e m D
4 5
Output:
Evry
Explanation:
The position of the given cell is (4, 5).
S1 = Evry.
S2 = EBtt.
S3 = Edm.
S4 = EDw.
There are two string values having the same maximum length Evry and EBtt.
The string Evry is the first occurring string. So it is printed as the output.
Example Input/Output 2:
Input:
10 7
E x e k e B h
e c j D b y e
j b l b t b d
h h C C h s d
D q j h d s d
n z s k D n h
l p i x k E D
b e a n b d v
b y d j y d d
t r y F u n u
8 2
Output:
eikdsd
#include<stdio.h>
#include <stdlib.h>
char* function(int row,int col,char arr[row][col],int var1P,int var2P,int var1,int var2){
    char* temp=malloc(row*col);
    int ind=0;
    while(var1P>=0 && var1P<row && var2P>=0 && var2P<col){
        temp[ind++]=arr[var1P][var2P];
        var1P+=var1;
        var2P+=var2;
    }
    temp[ind]='\0';
    return temp;
}
int main()
{
    int row,col;
    scanf("%d %d\n",&row,&col);
    
    char arr[row][col];
    for(int ele=0;ele<row;++ele){
        for(int j=0;j<col;++j){
            scanf("%col ",&arr[ele][j]);
        }
    }
    int Positioni,PositionJ;
    scanf("%d %d",&Positioni,&PositionJ);
    Positioni--;
    PositionJ--;
    char* answer;
    char* arr1=function(row,col,arr,Positioni,PositionJ,-1,-1);
    char* arr2=function(row,col,arr,Positioni,PositionJ,-1,1);
    char* arr3=function(row,col,arr,Positioni,PositionJ,1,1);
    char* arr4=function(row,col,arr,Positioni,PositionJ,1,-1);
    int l1=strlen(arr1),l2=strlen(arr2),l3=strlen(arr3),l4=strlen(arr4);
    if(l1>=l2 && l1>=l3 && l1>=l4){
        answer=arr1;
    }
    else if(l2>=l1 && l2>=l3 && l2>=l4){
        answer=arr2;
    }
    else if(l3>=l1 && l3>=l2 && l3>=l4){
        answer=arr3;
    }
    else{
        answer=arr4;
    }
    printf("%s",answer);
    return 0;
}
