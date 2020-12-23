Check All Vowels Present
The program must accept a string S. The program must print yes if all the vowels are present in S as the output. Else the program must print no as the output.
Note: All the alphabets in S are in lowercase.
Boundary Condition(s):
2 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The first line contains yes or no.
Example Input/Output 1:
Input:
tramiorue
Output:
yes
Explanation:
All the five vowels (aeiou) are present in tramiorue.
Hence yes is printed.
Example Input/Output 2:
Input:
rectangle
Output:
no
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char s[100],vowels[5]={'a','e','i','o','u'};
    int count=0;
    scanf("%s",s);
    for(int i=0;i<5;i++)
    {
        int present=0;
        for(int j=0;s[j]!=NULL;j++)
        {
            if(s[j]==vowels[i])
            {
                present=1;
            }
        }
        if(present==0)
        count++;
    }
    if(count==5)
    {
        printf("yes");
    }
    else
    {
        printf("no");
    }
}
