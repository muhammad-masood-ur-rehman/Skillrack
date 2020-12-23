Strong password check
Recently a security committee decided to enforce the following rules when an employee creates/changes his/her password.
->The password must contain atleast one special character among #$!_@
->The password must contain atleast two numbers
->The password must contain atleast one uppercase alphabet and one lower case alphabet
->The password must contain atleast minimum length of 8
->The password must contain atleast maximum length of 25
the program must accept a given password string P as input and check for these rules and output.
Example 1:
Input:
KiC_3b0x3r
Output:
VALID.
#include<stdio.h>
#include <stdlib.h>

int main()
{
char c;
int symbol=0,dig=0,upper=0,lower=0,leng=0,count=0;
while(scanf(“%c”,&c)>0)
{
if(c==’#’||c==’!’||c==’$’||c==’@’||c==’_’)
symbol++;
else if(isdigit(c))
dig++;
else if(c>=65&&c<=90)
upper++;
else if(c>=97&&c<=122)
lower++;

count++;
}
if(count>=8&&count<=25)
leng++;

if(symbol>=1&&dig>=2&&upper>=1&&lower>=1&&leng>0)
printf(“VALID”);
else
printf(“INVALID”);

}
