Identify correct operator
An expression E is passed as an input to the program.  The expression will contain three numbers A,B and C, one equal symbol and one of the mathematical operators +-*/
Example 1:
Input:
5-4=20
Output:
*
Explanation:
Only 5 multiplied with 4 gives 20. Hence – must be replaced with *.
Example 2:
Input:
999+9=111
Output:
/
#include<stdio.h>
#include <stdlib.h>

int main()
{
char c1,c2;
int a,b,c;
scanf(“%d%c%d%c%d”,&a,&c1,&b,&c2,&c);

if(a+b==c)
printf(“+”);
else if(a-b==c)
printf(“-“);
else if(a*b==c)
printf(“*”);
else
printf(“/”);

 

}
