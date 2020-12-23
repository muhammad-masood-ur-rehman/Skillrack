Pattern Printing num & *
Write a program that receives a number as input and prints it in the following format as shown below.
Examples:
Input:
6
Output:
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
16*17*18*19*20*21
16*17*18*19*20*21
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1
Output2:
1
2*3
4*5*6
4*5*6
2*3
1
Source code:
#include <stdio.h>

int main(void) {
            // your code goes here
int n,a=1,i,j;
scanf("%d",&n);
int m[n][n],k,l;
for(i=0;i<n;i++){
    for(j=0;j<=i;j++){
        m[i][j]=a;
        printf("%d",a++);
        if(j!=i){
        printf("*");
       // m[i][j]='*';
    }
}
printf("\n");
            }
            for(k=n-1;k>=0;k--){
                for(l=0;l<=k;l++){
                    printf("%d",m[k][l]);
                    if(l!=k)
                    printf("*");
                   
                }
                printf("\n");
            }
            return 0;
}
