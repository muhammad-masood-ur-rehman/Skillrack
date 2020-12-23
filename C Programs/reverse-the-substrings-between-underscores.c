Reverse the Substrings Between Underscores
Reverse the Substrings Between Underscores: String S is passed as the input. The String S may have zero or more underscores in it. The program must reverse the substrings between the underscore in S. 
Boundary Condition(s):
Length of the S from 3 to 100.
Input Format:
The first line contains the string S with substrings between underscores reversed.
Output Format:
The first line contains the string S modified based on the given conditions.
Example Input/Output 1:
Input:
abcd_efgh_ijke_mnl
Output:
abcd_hgfe_ekji_mnl
Example Input/Output 2:
Input:
_apple_mango
Output:
_elppa_mango
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char str[100];
    int l;
    scanf("%[^\n]%n",str,&l);
    int i=0;
    while(i<l){
        if(str[i]=='_'){
            int left=i+1;
            int right=i+1;
            while(right<l && str[right]!='_'){
                right++;
            }
            if(right==l)break;
            right--;
            while(left<right){
                char t=str[left];
                str[left]=str[right];
                str[right]=t;
                left++;right--;
            }
        }
        i++;
    }
    printf("%s",str);
}
Python:
a=input().strip()
l=[i for i in range(len(a))if a[i]=='_']
print(a[0:l[0]]+'_',end='')
for i in range(len(l)-1):print(a[l[i]+1:l[i+1]][::-1]+'_',end='')
print(a[l[-1]+1:])
