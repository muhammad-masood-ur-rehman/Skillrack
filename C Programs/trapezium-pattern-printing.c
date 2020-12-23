Trapezium Pattern Printing
Given an integer N as the input, print the pattern as given in the Example Input/Output section.
Input Format:
The first line contains N.
Output Format:
N lines containing the desired pattern.
Boundary Conditions:
2 <= N <= 100
Example Input/Output 1:
Input:
4
Output:
1*2*3*4*17*18*19*20
--5*6*7*14*15*16
----8*9*12*13
------10*11
Example Input/Output 2:
Input:
7
Output:
1*2*3*4*5*6*7*50*51*52*53*54*55*56
--8*9*10*11*12*13*44*45*46*47*48*49
----14*15*16*17*18*39*40*41*42*43
------19*20*21*22*35*36*37*38
--------23*24*25*32*33*34
----------26*27*30*31
------------28*29
#include <stdio.h>
void printPattern(int N)
{
    int s,i,j,lterm,rterm;
    lterm=1;
    rterm=N*N+1;
    int cou=2;
    for(i=N;i>0;i--){
        if(i!=N){
            for(s=0;s<cou;s++){
                printf("-");
            }
            cou+=2;
        }
        for(j=1;j<=i;j++){
            printf("%d",lterm);
            printf("*");
            lterm++;
        }
        for(j=1;j<=i;j++){
            printf("%d",rterm);
            if(j<i)
            printf("*");
            rterm++;
        }
        rterm=rterm-(i-1)*2-1;
        printf("\n");
    }

}
int main()
{
    int N;
    scanf("%d",&N);
    printPattern(N);
}
