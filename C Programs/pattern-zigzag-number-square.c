Pattern - ZigZag Number Square
Given an integer N as the input, print the pattern as given in the Example Input/Output section.
Input Format: The first line contains N.
Output Format: N lines containing the desired pattern.
Boundary Conditions:
2 <= N <= 50
Example Input/Output 1:
Input:
5
Output:
1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
Example Input/Output 2:
Input: 8
Output:
1 2 3 4 5 6 7 8
16 15 14 13 12 11 10 9
17 18 19 20 21 22 23 24
32 31 30 29 28 27 26 25
33 34 35 36 37 38 39 40
48 47 46 45 44 43 42 41
49 50 51 52 53 54 55 56
64 63 62 61 60 59 58 57
#include<stdio.h>
int main() {
    int N;
    scanf("%d",&N);
    int i,j,r,d=0;
    for(i=0;i<N;i++)
    {
        r=N*(i+1);
        d=r-N+1;
        if(i%2==0)
        {
            for(j=N-1;j>=0;j--)
                printf("%d ",d++);
        }
       else
        {
            for(j=0;j<N;j++)
                printf("%d ",r--);
        }
        printf("\n");
    }
}
