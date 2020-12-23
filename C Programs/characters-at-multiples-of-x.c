Characters at multiples of X
Example Input/Output 1:
Input:
abcdexyzwqpoolj
5
Output:
eqj
Explanation: The multiples of 5 are like 5, 10, 15,… So the characters in these positions are e,q,j
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
