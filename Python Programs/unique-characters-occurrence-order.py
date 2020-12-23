Unique Characters - Occurrence Order
Unique Characters - Occurrence Order: The program must accept a string S as input. The program must print the unique characters present in the string (remove duplicates) and print them in the order of their occurrence in the string S.
Boundary Condition(s):
1 <= Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the unique characters in S (in their order of their occurrence in S)
Example Input/Output 1:
Input:
100 apples
Output:
10 aples
from collections import OrderedDict
s=input()
print("".join(OrderedDict.fromkeys(s)))
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char s[1000],temp=1,c="";
    int i,j,k=0,n;
    scanf("%[^\n]",s);
    for(i=0;s[i];i++){
        if(!(s[i]==c)){
            for(j=i+1;s[j];j++){
                if(s[i]==s[j])
                s[j]=c;
            }
        }
    }
    for(i=0;s[i];i++){
        s[i]=s[i+k];
        if(s[i]==c){
            k++;
            i--;
        }
    }
    printf("%s",s);
}
