2D MATRIX MODIFICATION
A Matrix has R rows and C columns. Get the matrix as input and multiply the value in the cells of the matrix by a value E if it is even and multiply it by a value F if it is odd.
Input Format:
The first line contains R.The second line contains C.Next R lines containing the elements of the matrix with each column value seperated by a space.R+3 line contains E.R+4 line contains F.
Output Format:
R lines containing the elements of the revised matrix with each column value seperated by a space.
Boundary Conditions:1 <= R <= 1001 <= C <= 1001 <= E,F <= 100
Example Input/Output 1:
Input:
3 3
1 2 3
1 2 3
1 2 3
2 3
Output:
3 4 9
3 4 9
3 4 9
Example Input/Output 2:
Input:
4 5
12 19 16 18 12
2 12 14 5 12
8 3 17 4 19
18 11 5 14 9
2 5
Output:
24 95 32 36 24
4 24 28 25 24
16 15 85 8 95
36 55 25 28 45
#include<stdio.h> 
#include <stdlib.h>
 int main() {
 int a,b,i,j,m,n;
 scanf("%d %d",&a,&b); 
int ar[a][b]; for(i=0;i<a;i++){ 
for(j=0;j<b;j++){
 scanf("%d",&ar[i][j]);
 }
 }
 scanf("%d %d",&m,&n);
 for(i=0;i<a;i++){ 
for(j=0;j<b;j++){
 if(ar[i][j]%2==0) 
printf("%d ",ar[i][j]*m);
 else
 printf("%d ",ar[i][j]*n);
 } printf("\n"); 
}
}
