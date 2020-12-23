Sort the Vowels
The program must accept a string S as the input. The program must arrange the vowels in the string S in sorted order. Finally, the program must print the modified string S as the output.
Input : skillrack
Output : skallrick
Explanation:
After arranging the vowels in the string skillrack in sorted order, the string becomes skallrick.
Hence the output is skallrick
Here are the various methods and logic.
C :
//C logic by @ Agent Natasha
#include<stdio.h>
#include <stdlib.h>
int main()
{
int num,m,ind,j=0;
char s[100],s1[100];
scanf("%s",s);
num=strlen(s);
//storing the vowels in another array
for(ind=0;ind<num;ind++)
{
   if(s[ind]=='a' || s[ind]=='e' || s[ind]=='i' || s[ind]=='o' || s[ind]=='u' || s[ind]=='A' || s[ind]=='E' || s[ind]=='I' || s[ind]=='O' || s[ind]=='U')
   {
       s1[j]=s[ind];
       j++;
   }
}
//sorting the array with vowels in ascending order
for(ind=0;ind<j;ind++)
{
   for(m=0;m<j;m++)
   {
       if(s1[ind]<s1[m])
       {
           char c=s1[ind];
           s1[ind]=s1[m];
           s1[m]=c;
       }
   }
}
j=0;//printing the sorted array
for(ind=0;ind<num;ind++)
{
   if(tolower(s[ind])=='a' || tolower(s[ind])=='e' || tolower(s[ind])=='i' || tolower(s[ind])=='o' || tolower(s[ind])=='u')
   {
       printf("%c",s1[j]);
       j++;
   }
   else
   printf("%c",s[ind]);
}
}
//C logic by @ Agent Marvel
#include<stdio.h>
#include <stdlib.h>
int main()
{
    char string[1001],temp;
    scanf("%s",string);
    int n=strlen(string);
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if((tolower(string[i])=='a' || tolower(string[i])=='e' || tolower(string[i])=='i' || tolower(string[i])=='o' || tolower(string[i])=='u') && (tolower(string[j])=='a' || tolower(string[j])=='e' || tolower(string[j])=='i' || tolower(string[j])=='o' || tolower(string[j])=='u'))
            {
                if(string[i]>string[j])
                {
                    temp=string[i];
                    string[i]=string[j];
                    string[j]=temp;
                }
            }
        }
    }
    for(int i=0;i<n;i++)
    {
        printf("%c",string[i]);
    } 
}
//C logic by @ Agent Steve
#include<stdio.h>
#include <stdlib.h> 
int isVow(char ch){
      ch=tolower(ch);
      return ch=='a' || ch=='e'  ||  ch =='i'   || ch=='o'  ||  ch=='u';
}
char printVow(int sortedVowels[],int ind){
	while(!sortedVowels[ind])ind++;
      	sortedVowels[ind]--;
     	return ind;
}
int main()
{
    	char str[100];
    	scanf("%s",str);
	int sortedVowels[256]={0};
     	for(int i=0;i<strlen(str);++i)     isVow(str[i])) sortedVowels[str[i]]++;
     	static int ind=0;
     	for(int i=0;i<strlen(str);++i)	printf("%c",!isVow(str[i]) ? str[i]: printVow(sortedVowels,ind));
}
Python :
#Python logic by @Agent Parker
s=input().strip()
b='aeiouAEIOU'
c=[]
for i in s:
   if i in b:c.append(i)
c.sort()
k=0
for i in s:
   if i in b:
       print(c[k],end='')
       k+=1
   else:print(i,end='')
#Python logic by @Agent Stark
n=input()
vowel='aeiouAEIOU'
v=[]
for i in range(len(n)):
   if n[i] in vowel:
   v.append(n[i])
v=sorted(v)
h=0
for i in n:
  if i in vowel:
     print(v[h],end="")
     h+=1
   else:
     print(i,end="")
#Python logic by @Agent Quill
s="aeiouAEIOU"
s1=input();l=[]
for i in s1:
   if i in s:
       l.append(i) 
l.sort();k=0
for i in s1:
   if i in s:
       print(l[k],end='')
       k+=1 
   else:
       print(i,end='')
