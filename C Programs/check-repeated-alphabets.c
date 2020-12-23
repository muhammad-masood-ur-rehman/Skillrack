Check Repeated Alphabets
The program must accept a string value S as the input. The program must print invalid if the alphabets are repeated continuously for more than two times. Else the program must print valid as the output.
Boundary Condition(s):
3 <= Length of S <= 100
Input Format:
The first line contains the values of string S.
Output Format:
The first line contains either invalid or valid.
Example Input/Output 1:
Input:
dreaaam
Output:
invalid
Explanation:
In dreaaam, a is repeated more than two times continuously.
Hence the output is invalid
Example Input/Output 2:
Input:
skillrack
Output:
valid
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char s[100];
    int i,repeat=0;
    scanf("%s",s);
    for(i=0;s[i]!=NULL;i++)
    {
        if(s[i]==s[i+1]&&s[i]==s[i+2])
        {
            repeat++;
        }
    }
    if(repeat==0)
    {
        printf("valid");
    }
    else
    {
        printf("invalid");
    }
       
}
