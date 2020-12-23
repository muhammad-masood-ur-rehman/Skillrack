Replace Vowels - Circular Fashion
The program must accept a string S as the input. The program must replace all the vowels in S by the vowels a, e, i, o and u in a circular manner. Finally, the program must print the modified string as the output.
Note: All the alphabets in S are only in lower case.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains the string value S.
Output Format:
The first line contains the modified string value of S.
Example Input/Output 1:
Input:
kingkong
Output:
kangkeng
Explanation:
The vowels in the string kingkong are i and o. So they are replaced by a and e.
Hence the output is kangkeng
Example Input/Output 2:
Input:
icecreamchocolate
Output:
acecriomchucaleti
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char s[100],a[5]={'a','e','i','o','u'};
    int j=0,i;
    scanf("%s",s);
    for(i=0;s[i]!=NULL;i++)
    {
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u')
        {
            s[i]=a[j];
            j++;
        }
        if(j>5)
        {
            j=0;
        }
    }
    printf("%s",s);
    return 0;

}
