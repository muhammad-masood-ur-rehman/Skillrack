String – Count Articles
A string S is passed as the input. The program must print the number of articles in S. The string S passed as the input NEEDNOT be corrected grammatically.
Example 1:
Input:
I went to a movie yesterday along with an old man.
Output:
2
#include<stdio.h>
#include <stdlib.h>

int main()
{
char str[1000],str1[1000];
int count=0;

while(scanf(“%s”,&str)>0)
{

if(strcmp(str,”a”)==0||strcmp(str,”an”)==0||strcmp(str,”the”)==0)
count++;
}

printf(“%d\n”,count);

}
import string
n,d=input(),0
for c in string.punctuation:
    n=n.replace(c," ")
s=[i for i in n.split()]
for i in range(len(s)):
    if s[i]=='the' or s[i]=='a' or s[i]=='an':
          d+=1

print(d)   
