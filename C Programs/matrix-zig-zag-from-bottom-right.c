Matrix Zig-Zag from Bottom Right
The program must accept an integer matrix of size R*C as the input. The program must print the elements from the bottom right of the matrix in diagonally zig-zag order.
Boundary Condition(s):
2 <= R, C <= 100
Input Format:
The first line contains R and C separated by a space.
The next R lines, each containing C integers separated by a space.
Output Format:
The first line contains all R*C elements in diagonally zig-zag order, with the elements separated by a space.
Example Input/Output 1:
Input:
3 7
44 23 14 62 34 24 29
18 66 22 77 14 51 60
13 67 35 26 34 40 72
Output:
72 60 40 34 51 29 24 14 26 35 77 34 62 22 67 13 66 14 23 18 44
Example Input/Output 2:
Input:
4 4
6 7 5 8
8 3 2 1
9 1 2 6
5 4 5 1
Output:
1 6 5 4 2 1 8 2 1 5 9 3 5 7 8 6
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int r,c;
    scanf("%d%d",&r,&c);
    int arr[r][c];
    
    for(int i=0;i<r;++i){
        for(int j=0;j<c;++j){
            scanf("%d",&arr[i][j]);
        }
    }
    int i=r-1,j=c-1,counter=1;
    
    while(i!=0 || j!=0){
        printf("%d ",arr[i][j]);
        
        if(counter){
            i--;j++;
        }
        else{
            i++;j--;
        }
        
        if(j>=c || i<0){
            if(i<0){
                i++;j--;
            }
            j--;
            counter=!counter;
        }
        else if(i>=r || j<0){
            if(j<0){
                i--;j++;
            }
            i--;
            counter=!counter;
        }
    }
    printf("%d ",arr[i][j]);
}
