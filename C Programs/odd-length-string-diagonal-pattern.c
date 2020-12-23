Odd Length String Diagonal Pattern
An odd length string S of length is passed as the input. The program must print the string S as two diagonal as shown in the example input/output below
Example 1:
Input:
cry
Output:
c y
r
c y
Example 2:
Input:
 tiger

Output:
 t   r
  i g
   e
  i g
 t   r
#include<stdio.h>
#include <stdlib.h>

int main()
{
 char str[1000];
 scanf("%s",str);
 int len = strlen(str);
 
 for(int i=0;i<len;i++)
 { 
 int g=len-i-1;
 for(int j=0;j<len;j++)
 { 
 if(i==j)
 printf("%c",str[j]);
 else if(j==g)
 printf("%c",str[j]);
 else
 printf(" ");
 
 }
 printf("\n");
 }

}
