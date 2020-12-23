Character B follows A
Given a string S and two characters A, B the program must print the number of occurrences where A is followed by B.
Example 1:
Input:
malayalam
a
l
Output:
2
Explanation:
The two occurrence where a is followed by l is a highlighted below malayalam.
#include<stdio.h>
#include <stdlib.h>

int main()
{
char str[1000];
char first[2],last[2];
int count=0;
scanf(“%s”,str);
scanf(“%s”,first);
scanf(“%s”,last);

for(int i=0;i<strlen(str);i++)
if(str[i]==first[0]&&str[i+1]==last[0])
count++;

printf(“%d”,count);


}
