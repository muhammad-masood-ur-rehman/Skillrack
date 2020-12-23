String Tree Pattern
Given a String S as the input, the program must print the characters present in the string S as shown in the Example Input/Output section.
Boundary Conditions:
1 <= Length of S <= 100
Input Format:
The first line contains the string S.
Output Format:
The characters of S and * as shown in the Example Input/Output section.
Example Input/Output:
Input:
abcd
Output:
a
**
bbb
****
ccccc
******
ddddddd

#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[100];
    int i,j;
    scanf("%s",S);
    for(i=0;i<2*strlen(S)-1;i++)
    {
        for(j=0;j<=i;j++)
        {
            if(i%2==0)
                printf("%c",S[i/2]);
            else
                printf("*");
        }
        printf("\n");
    }
}
