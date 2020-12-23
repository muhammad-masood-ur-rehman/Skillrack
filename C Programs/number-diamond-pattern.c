Number Diamond Pattern
Given an integer N as the input, the program must print the pattern as mentioned in the Example Input/Output Section.
Boundary Condition(s):
1 <= N <= 50
Input Format:
The first line contains the value of N.
Output Format:
The list of lines contain the pattern as shown in the Example Input/Output Section.
Example Input/Output 1:
Input:
4
Output:
* * * * 0 * * * * 
* * * 0 1 0 * * * 
* * 0 1 2 1 0 * * 
* 0 1 2 3 2 1 0 * 
0 1 2 3 4 3 2 1 0 
* 0 1 2 3 2 1 0 * 
* * 0 1 2 1 0 * * 
* * * 0 1 0 * * * 
* * * * 0 * * * * 
Example Input/Output 2:
Input:
5
Output:
* * * * * 0 * * * * * 
* * * * 0 1 0 * * * * 
* * * 0 1 2 1 0 * * * 
* * 0 1 2 3 2 1 0 * * 
* 0 1 2 3 4 3 2 1 0 * 
0 1 2 3 4 5 4 3 2 1 0 
* 0 1 2 3 4 3 2 1 0 * 
* * 0 1 2 3 2 1 0 * * 
* * * 0 1 2 1 0 * * * 
* * * * 0 1 0 * * * * 
* * * * * 0 * * * * * 
#include<stdio.h>
#include <stdlib.h>
void print(int n){
    while(n--)printf("* ");
    return;
}
int main()
{
    int n;
    scanf("%d",&n);
    
    for(int itr=1;itr<=(n*2)+1;++itr){
        print(itr <= n+1 ? n-itr+1 : itr-n-1 );
        for(int i=0;i< (itr<=n+1 ? itr : (n-(itr-n)+2));++i){
            printf("%d ",i);
        }
        for(int i= itr<=n+1 ? itr-2 :(n-(itr-n)) ;i>=0;i--)
        printf("%d ",i);
        print(itr <= n+1 ? n-itr+1 : itr-n-1 );
        printf("\n");
    }
    return 0;
}
