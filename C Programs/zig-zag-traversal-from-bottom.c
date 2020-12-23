Zig Zag Traversal From Bottom
Zig Zag Traversal From Bottom: Given an integer a matrix of size M x N, print the elements of the matrix in zig zag order from bottom.
Boundary Condition:
1<= M, N <= 100
Input Format:
The first line contains the integer M and N separated by space.
The next M lines contain the matrix values.
Output Format:
The first line contains all the elements in zig zag order from bottom.
Sample Input/Output 1:
Input:
3 3
1 2 3
4 5 6
7 8 9 
Output:
9 6 8 7 5 3 2 4 1
Sample Input/Output 2:
Input:
3 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
Output:
15 10 14 13 9 5 4 8 12 11 7 3 2 6 1
include<stdio.h>
#include <stdlib.h>

int main()
{
    int r,c;
    scanf("%d%d",&r,&c);
    int counter=1;
    int arr[r][c];
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    int i=r-1,j=c-1;
    while(i>=0 && j>=0){
        printf("%d ",arr[i][j]);
        if(counter){
            //is in border
            if(j==c-1 || i==0){
                i==0 ? j-- : i--;
                counter=0;
            }
            else{
                i--;j++;
            }
        }
        else{
            if(j==0 || i==r-1){
                j==0 ? i--: j--;
                counter=1;
            }
            else{
                i++;j--;
            }
        }
    }
}
