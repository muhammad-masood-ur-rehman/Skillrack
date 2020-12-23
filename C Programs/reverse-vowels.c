String - Reverse Vowels
Given a string S, reverse only the vowels in the string S and print the resultant string R as the output. The consonants must maintain their original locations in S.
Input Format:
The first line contains S.
Output Format:
The first line contains R.
Boundary Conditions:
Length of S is from 2 to 500.
Example Input/Output 1:
Input:
idea
Output:
adei
Example Input/Output 2:
Input:
hello
Output:
holle
#include<stdio.h>
#include <stdlib.h>
int isVow(char ch){
    ch=tolower(ch);
    return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}
int main()
{
    int l,left=0,right;
    char str[500];
    scanf("%s%n",str,&l);
    right=l-1;
    while(l){
        if(!isVow(str[left]) && l--)printf("%c",str[left++]);
        else if(isVow(str[right]) && l--){
            printf("%c",str[right--]);
            left++;
        }
        else{
            right--;
        }
    }

}
