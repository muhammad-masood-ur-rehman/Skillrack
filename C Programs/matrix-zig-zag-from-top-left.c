Matrix Zig-Zag from Top Left
The program must accept an integer matrix of size R*C as the input. The program must print the elements from the top left of the matrix in diagonally zig-zag order.
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
1 9 3 9 4 7 2
4 5 2 4 8 3 5
9 3 6 3 5 1 8
Output:
1 9 4 9 5 3 9 2 3 6 4 4 7 8 3 5 3 2 5 1 8
Example Input/Output 2:
Input:
4 4
29 76 80 57
18 69 47 36
36 26 68 61
48 34 30 82
Output:
29 76 18 36 69 80 57 47 26 48 34 68 36 61 30 82
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
    int counter=0;
    int i=0,j=0;
    while(i!=r-1 || j!=c-1){
        printf("%d ",arr[i][j]);
        if(counter){
            i++;j--;
        }
        else{
            i--;j++;
        }
        if(j<0 || i>=r){
            if(i>=r){
                i--;j++;
            }
            j++;
            counter=!counter;
        }
        else if(i<0 || j>=c){
            if(j>=c){
                j--;i++;
            }
            i++;
            counter=!counter;
        }
        
    }
    printf("%d ",arr[r-1][c-1]);
}
