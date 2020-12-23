Common Part in string values
Two string values S1 and S2 are passed as input. The last portion of S1 will be the first portion of S2. The program must print this common part in S1 and S2.
Example 1:
Input:
mayday
daybreak
Output:
day
#include<stdio.h>
#include <stdlib.h>

int main()
{
 char str1[1000],str2[1000];
 scanf("%s%s",str1,str2);
 
 int len1 = strlen(str1);
 
 int s1 = len1 - 1;
 int s2 = 0;
 
 while(s1 >= 0)
 {
 if(str1[s1] != str2[s2])//last character of str1[5] ==str2[0]
 {
 s2++;
 }
 else
 {
 if(str1[s1-1] == str2[s2] )//str[4]==str[1]
 {
 s1--;
 s2++;
 }
 else
 break;
 }
 
 }
 
 for(int k=0;k<=s2;k++)
 printf("%c",str2[k]);
 
 
}
