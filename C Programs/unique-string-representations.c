Unique String Representations
Given a string S print the number of unique string values that can be formed by rearranging the letters in the string S.
Boundary Condition:
2 <= Length of S <= 22 
Input/Output Format:
Input:
First line contains the string S.
Output:
The value representing the number of unique string values that can be formed by rearranging the letters in the string S.
Example Input/Output 1:
Input:
abc
Output:
6
Example Input/Output 2:
Input:
apple
Output:
60
#include<stdio.h>
#include <stdlib.h>

int main()
{
char s[22];
scanf("%s",s);
unsigned long long l=strlen(s);
unsigned long long i,j,c,x=1,t=1,flag=0;
for(i=0;i<l;i++)
{
    c=1;
    for(j=i+1;j<l;j++)
    {
        if(s[i]==s[j]&&s[j]!='*')
        {
            c++;
            s[j]='*';
        }
    }
    s[i]='*';
    unsigned long long m=1;
    if(c!=1)
    {
        for(int k=1;k<=c;k++)
        {
            m*=k;
        }
        t*=m;
    }
}
for(i=1;i<=l;i++)
{
    if(i%10==0)
    {
        flag++;
    }
    else
    {
        x*=i;
    }
    if(i==20)
    {
        x*=2;
    }
}
printf("%llu",x/t);
if(flag==1)printf("0");
if(flag==2)printf("00");
}
