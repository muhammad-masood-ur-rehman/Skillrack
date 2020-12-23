Word Search in Matrix
The program must accept a character matrix of size R*C and a string S as input. The program must search the string S in the given R*C character matrix by traversing horizontally and vertically. If the string S is found in the matrix, the program must print yes. Else the program must print no as the output.
Boundary Condition(s):
2 <= R, C, Length of S <= 50
Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C characters separated by a space.
The (R+2)nd line contains the string S.
Output Format:
The first line contains the either yes or no.
Example Input/Output 1:
Input:
5 8
k e r t u n o p
r a i n q b o w
v a n g u e c l
r a t t o n g h
h w y f n x o g
ringtone
Output:
yes
Explanation:
Here, the string ringtone is found in the given matrix and it is highlighted below.
k e r t u n o p
r a i n q b o w
v a n g u e c l
r a t t o n g h
h w y f n x o g
Example Input/Output 2:
Input:
4 7
p o k r a n w
m e n e e r l
j h g i n o v
a d f q s t c
engineering
Output:
no
#include<stdio.h>
#include <stdlib.h>
// int dfs()
int r,c;
char check[50];
int dfs(char arr[r][c],int i,int j,int ind){
    if(check[ind]=='\0')return 1;
    if(i>-1 && j>-1 && i<r && j<c && arr[i][j]==check[ind] && arr[i][j]!='*'){
        char store=arr[i][j];
        arr[i][j]='*';
        if( dfs(arr,i+1,j,ind+1) )return 1;
        if( dfs(arr,i-1,j,ind+1) )return 1;
        if( dfs(arr,i,j+1,ind+1) )return 1;
        if( dfs(arr,i,j-1,ind+1) )return 1;
        
        arr[i][j]=store;
    }
    return 0;
}
int main()
{
    scanf("%d %d\n",&r,&c);
    char arr[r][c];
    
    for(int i=0;i<r;++i){
        for(int j=0;j<c;++j){
            scanf("%c ",&arr[i][j]);
        }
    }
    scanf("%s",check);
    
    for(int i=0;i<r;++i){
        for(int j=0;j<c;++j){
            if(arr[i][j]==check[0]){
                if(dfs(arr,i,j,0)){
                    printf("yes");
                    return 1;
                }
            }
        }
    }
    
    printf("no");
    
    return 1;
}
