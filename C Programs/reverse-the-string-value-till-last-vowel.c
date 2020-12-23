Reverse the string value till last vowel
Reverse the string value till last vowel
Given a string S, the program must reverse the string till last vowel. (All alphabets will be in smaller case and there will be no space within the string S).
Input Format:
The first line contains S.
Output Format:
The first line contains the string value reversed till last vowel
Boundary Conditions:
2 <= Length of S <= 100
Example Input/Output 1:
Input:
manager
Output:
eganamr
Explanation:
The last vowel is e. Hence manage is reversed and r is retained as such.
#include<stdio.h>
#include <stdlib.h>

int main()
{
char s[100];
scanf("%s",s);
int index = 0,i=0,j=0;
for(i=strlen(s)-1;i>=0;i--)
{
    if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
    {
        index = i;
        break;
    }
}
//printf("%d", index);
for(i=index;i>=0;i--)
printf("%c",s[i]);
for(j=index+1;j<strlen(s);j++)
printf("%c",s[j]);

}
