Maximum Length - S1 and S2
The program must accept two string values S1 and S2 as the input. The program must print the string having the maximum length as the output. If both the string values having the same length then print both the string values in the given order as the output.
Boundary Condition(s):
1 <= Length of S1, S2 <= 100
Example Input/Output 1:
Input:
rack
skill
Output:
skill
Example Input/Output 2:
Input:
Master
Chrome
Output:
Master
Chrome
#include<stdio.h>
#include<string.h>

int main()
{
    char str1[101], str2[101];
    scanf("%s %s", str1, str2);
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    if(len1 >= len2)
    {
        printf("%s\n", str1);
    }
    if(len2 >= len1)
    {
        printf("%s\n", str2);
    }
    return 0;
}
a,b=input().strip(),input().strip()
if len(a)>len(b): print(a)
elif len(a)==len(b): 
     print(a) 
     print(b)
else: print(b)
