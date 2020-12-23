Pattern Printing - WIPR 001
Given an input value of N, complete the method printPattern so that program prints the pattern as given in example Input/Output.
Input Format:
The first line contains the value of the N.
Output Format:
The N lines contain the pattern as given in the example Input/Output.
Boundary Conditions:
4 <= N <= 100
Example Input/Output 1:
Input:
5
Output:
1
3 2
4 5 6
10 9 8 7
11 12 13 14 15
Example Input/Output 2:
Input:
10
Output:
1
3 2
4 5 6
10 9 8 7
11 12 13 14 15
21 20 19 18 17 16
22 23 24 25 26 27 28
36 35 34 33 32 31 30 29
37 38 39 40 41 42 43 44 45
55 54 53 52 51 50 49 48 47 46
#include <stdio.h>
#include <stdlib.h>
void printPattern(int N)
{
    int end=0,c=1;
    for(int i=1;i<=N;++i){
        int var= end+(c==-1 ? i : 1);
        for(int j=0;j<i;++j){
            printf("%d ",var+(j*c));
        }
        end=c==1 ? var+i-1 : var;
        c=c==1? -1 : 1;
        printf("\n");
    }
}
int main()
{
    int N;
    scanf("%d",&N);
    printPattern(N);
}
