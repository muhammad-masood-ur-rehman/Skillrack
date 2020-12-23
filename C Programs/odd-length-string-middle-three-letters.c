Odd Length String – Middle Three Letters
An odd length string S is passed as the input.  The middle three letters of S must be printed as the output.
Example 1;
Input:
level
Output:
eve
Example 2:
Input:
manager
Output:
nag
#include<stdio.h>
#include <stdlib.h>

int main()
{
char str[1000];
scanf(“%s”,str);
int middle=strlen(str)/2;
printf(“%c%c%c”,str[middle-1],str[middle],str[middle+1]);
}
