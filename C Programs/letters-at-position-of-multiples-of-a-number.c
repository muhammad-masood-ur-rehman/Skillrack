Letters at position of multiples of a number
A string of length L consists of characters is passed as input to the program. A given number N is also passed as the input to the program. The program must print the characters at the positions which are multiples of the given number.
Input Format:
The first line will contain the string of length L.
The second line will contain the number N.
Boundary Conditions:
3 <= L <= 50
1 <= N <= 30
Output Format:
The characters at the positions which are multiples of the given number.

Example Input/Output 1:
Input:
abcdef
3
Output:
cf
Explanation:
Multiples of 3 are like 3,6,9,...
So the characters at positions 3,6 namely c and f are printed as output.

Example Input/Output 2:
Input:
environment
2
Output:
niomn
Explanation:
As it must be multiples of 2, the characters at even positions are printed as output.
#include<stdio.h>
#include <stdlib.h>
#include<string.h>
int main()
{
    char str[100];
    int x,i;
    fgets(str,100,stdin);
    scanf("%d",&x);
    for(i=1;i<=strlen(str);i++)
    {
       if(i%x==0)
        printf("%c",str[i-1]);
    }

}
