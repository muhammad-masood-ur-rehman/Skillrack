Infected Crops
Infected Crops: A farm is represented as a R*C 2D matrix. Due to the soil condition, some crops are very weak. These crops are vulnerable to insects. The weak crops are represented by W and good crops are representedby G. When a crop is infected, the weak crops adjacent to it (in all directions north, south, east and west) are also infected and destroyed. The crops which are already infected are represented as I in the input.
Boundary Condition:
1<= R,C <= 50
Input Format:
First line contains R and C separated by space.
Next R lines contain the matrix representation of the farm.
Output Format:
The first R lines contain the farm status with the destroyed crops represented by D, weak crops by W and good crops by G.
Sample Input/Output 1:
Input:
3 3
W G W
W G G
W I G
Output:
D G W
D G G
D D G
Sample Input/Output 2:
Input:
5 5
W W G W W
I W G G G
G W G G G
I G I W W
G G W G W
Output:
D D G W W 
D D G G G 
G D G G G 
D G D D D 
G G D G D 
#include <stdio.h>
void k(int i,int j,int r,int c,char str[r][c])
{
    if(i>=r||i<0||j>=c||j<0||str[i][j]=='G'||str[i][j]=='D')
    return;
    if(str[i][j]=='W'||str[i][j]=='I'){
        str[i][j]='D';
        k(i+1,j,r,c,str);
        k(i-1,j,r,c,str);
        k(i,j+1,r,c,str);
        k(i,j-1,r,c,str);
    }
}
int main(){
    int r,c,i,j;
    scanf("%d%d",&r,&c);
    char str[r][c];
    for(i=0;i<r;i++){
        for(j=0;j<c;j++)
        scanf(" %c ",&str[i][j]);
    }
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            if(str[i][j]=='I'){
                k(i,j,r,c,str);
            }
        }
    }
    printf("\n");
    for(i=0;i<r;i++){
        for(j=0;j<c;j++)
        printf("%c ",str[i][j]);
        printf("\n");
    }
}
