String - Alphabets Frequency
Given a string S as the input, print the count of distinct alphabets in S followed by their frequency of occurrence. The upper case alphabets must be followed by the lower case alphabets.
Input Format:
The first line contains S.
Output Format:
The first line contains the alphabets and their occurrence count (Upper case alphabets followed by lower case alphabets)
Boundary Conditions:
2 <= LENGTH of S <= 200
Example Input/Output 1:
Input:
ApPleJuice
Output:
A1J1P1c1e2i1l1p1u1
Example Input/Output 2:
Input:
igotupat9:00aminthemorning
Output:
a2e1g2h1i3m2n3o2p1r1t3u1
#include <stdio.h>
void printAlphabetCount(char strval[])
{
    int arr[256]={0};
    int l=strlen(strval);
    for(int i=0;i<l;i++)arr[strval[i]]++;
    
    for(char ch='A';ch<='Z';ch++)if(arr[ch])printf("%c%d",ch,arr[ch]);
    for(char ch='a';ch<='z';ch++)if(arr[ch])printf("%c%d",ch,arr[ch]);
}
void main()
{
    char strval[200];
    scanf("%s", strval);
    printAlphabetCount(strval);
}
