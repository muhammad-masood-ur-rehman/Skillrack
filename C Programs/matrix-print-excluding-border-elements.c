Matrix Print Excluding Border elements
A matrix of size N*N is passed as input. The program must print the matrix excluding the elements present at the border of the matrix.
Boundary Condition(s):
3 <= N <= 100
Input Format:
The first line contains the value of N.
The next N lines contain N elements each separated by space(s).
Output Format:
The first N-2 lines contain the matrix without the border elements.
Example Input/Output 1:
Input:
3
1 2 3
4 5 6
7 8 9
Output:
5
Example Input/Output 2:
Input:
5
33 56 23 88 29
384 388 392 58 30
93 63 272 223 75
95 338 44 87 90
94 22 21 67 43
Output:
388 392 58 
63 272 223 
338 44 87
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j){
            int num;
            scanf("%d",&num);
            if(i!=0 && i!=n-1 && j!=0 && j!=n-1)printf("%d ",num);
        }
        if(i!=0 && i!=n-1)printf("\n");
    }

}
