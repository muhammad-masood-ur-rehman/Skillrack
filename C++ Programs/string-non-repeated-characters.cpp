String - Non Repeated Characters
The program must accept a string S as the input. The program must print all the non-repeated characters in the string S in the order of their occurrence as the output.
Note: At least one non-repeated character is always present in the string S.
Boundary Condition(s):
1 <= Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the non-repeated characters in the string S separated by a space.
Example Input/Output 1:
Input:
Japan
Output:
J p n
Explanation:
Here the string is Japan.
The characters J, p and n are not repeated in the string Japan.
Hence the output is J p n
Example Input/Output 2:
Input:
fireFighter
Output:
f F g h t
C++:
#include <iostream>
using namespace std;
int main()
{
    char string[1001];
    cin>>string;
    int a[128]={0};
    for(int i=0;string[i];i++)
    {
        a[string[i]]++;
    }
    for(int i=0;string[i];i++)
    {
        if(a[string[i]]==1)
        {
            cout<<string[i]<<" ";
        }
    }
}
C:
#include<stdio.h>
#include <stdlib.h>
int main()
{
int hash[256]={0},index;
char string[1001];
scanf("%s",string);
for(index=0;index<strlen(string);index++)
hash[string[index]]++;
for(index=0;index<strlen(string);index++)
if(hash[string[index]]==1)
{
printf("%c ",string[index]);
}
}
#include<stdio.h>
#include <stdlib.h>
int main()
{
    char str[1000];
    scanf("%s",str);
    int hash[256]={0};
    for(int i=0;i<strlen(str);++i)hash[str[i]]++;
    for(int i=0;i<strlen(str);++i)if(hash[str[i]]==1)printf("%c ",str[i]);
}
#include<stdio.h>
#include <stdlib.h>
int main()
{
    char string[10001];
    scanf("%s",string);
    int length=strlen(string),count[128]={0};
    for(int ind=0;ind<length;ind++)
    {
        count[string[ind]]++;
    }
    for(int ind=0;ind<length;ind++)
    {
        if(count[string[ind]]==1)
        {
            printf("%c ",string[ind]);
        }
        count[string[ind]]++;
    }
}
Python:
s=input().strip();d=[]
d=[i for i in s if s.count(i)==1]
print(*d)
string=input().strip()
array=[]
for i in string:
    if string.count(i)<=1: 
        array.append(i)
for i in array:
    print(i,end=" ")
st=input().strip() 
for ele in st: 
    if st.count(ele)==1: 
        print(ele,end=" ")
st=input().strip() 
[print(ele,end=" ") for ele in st if st.count(ele)==1]
a=input().strip()
l=[a.count(i) for i in a]
for i in range(len(a)):
   if l[i]==1:
      print(a[i],end=' ')
