String Reverse First and Second Half
A string is passed as input. The program must reverse the first and second half of the string and print it. Assume that the size of the string is divisible by two.
Boundary Condition(s):
1 <= Length of string <= 1000
Input Format:
The first line contains the string.
Output Format:
The first line contains the reversed string.
Example Input/Output 1:
Input:
computer
Output:
pmocretu
Example Input/Output 2:
Input:
window
Output:
niwwod
C:
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char a[1000];
    scanf("%s",a);
    int ele,l=strlen(a), b=strlen(a)/2;
    for(ele=b-1;ele>=0;ele--)
    printf("%c",a[ele]);
    for(ele=l-1;ele>=b;ele--)
    printf("%c",a[ele]);
    
}
#include<stdio.h>
#include <stdlib.h>
int main()
{
    char s1[1000];
    scanf("%s\n",s1);
    
    int l=strlen(s1);
    int mid=l/2;
    for(int i=0;i<mid/2;++i){
        char t=s1[mid-i-1];
        s1[mid-i-1]=s1[i];
        s1[i]=t;
        
        t=s1[mid+i];
        s1[mid+i]=s1[l-i-1];
        s1[l-i-1]=t;
    }
    printf("%s",s1);
}
