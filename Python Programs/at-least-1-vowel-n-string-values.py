At least 1 Vowel - N String Values
The program must accept N string values as the input. The program must print yes if all the N string values contain at least 1 vowel. Else the program must print no as the output.
Example Input/Output 1:
Input:
4
lion
TIGER
elEphant
Deer 
Output:
yes
Explanation:
The number of vowels in the string lion is 2.
The number of vowels in the string TIGER is 2.
The number of vowels in the string elEphant is 3.
The number of vowels in the string Deer is 2.
Here all the 4 string values contain at least 1 vowel.
Hence the output is yes
Example Input/Output 2:
Input:
5
Land
Earth
SKY
Water
FIRE
Output:
no
Python:
n=int(input()) 
li=[] 
for ele in range(n): 
    li. append(input ().strip()) 
 li2=[] 
 al="aeiouAEIOU" 
 for ele in li: 
    r=0 
    for foo in ele: 
        if foo in al: 
            r+=1 
    if r>0: 
        li2.append(1) 
if len(li2)==n:
     print("yes")
else:
     print("no")
n=int(input()) 
li=[]
v,c=0,0 
for ele in range(n): 
    li. append(input ().strip()) 
for ele in li:
    for foo in ele:
       if foo in "aeiouAEIOU":
           v+=1
    if v>=1:
       c+=1
    v=0
if (c==n):
     print("yes")
else:
     print("no")
def vowel(n):
    ct=0
    for ele in n:
        if ele in 'aeiouAeiou':
            ct+=1
    return ct
n=int(input())
li=[]
l=0
for ele in range(n):
    s=input().strip()
    count=vowel(s)
    li.append(count)
for ele in li:
    if ele>=1:
        l+=1
if l==len(li):
    print("yes")
else:
    print("no")
C:
#include<stdio.h>
#include <stdlib.h>
int isvowel(char ch)
{
    ch=tolower(ch);
    return ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u';
}
int main()
{
char string[101];
int i,j,cmp,num;
scanf("%d",&num);
for(i=0;i<num;i++)
{
    scanf("%s ",string);
    cmp=0;
    for(j=0;j<strlen(string);j++)
    if(isvowel(string[j])==1){
    cmp=1;
    break;
    }
    if(cmp==0)
    {
        printf("no");
        return 0;
    }
}
printf("yes");
}
#include<stdio.h>
#include <stdlib.h>
int main()
{
    int no_of_strings,count=0;
    scanf("%d",&no_of_strings);
    char string[101][101];
    for(int ind=0;ind<no_of_strings;ind++)
    {
        scanf("%s ",string[ind]);
    }
    for(int ind=0;ind<no_of_strings;ind++)
    {
        int sub_count=0;
        for(int ind2=0;ind2<strlen(string);ind2++)
        {
            char temp_char=toupper(string[ind][ind2]);
            if(temp_char=='A' || temp_char=='E' || temp_char=='I' || temp_char=='O' || temp_char=='U' )
            {
                sub_count=1;
            }
        }
        if(sub_count==1)
        {
            count+=1;
        }
    }
    if(count==no_of_strings)
     printf("yes");
    else
     printf("no");
}
