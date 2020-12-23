C - Functions - Vowel Count
[pwa-install-button] 
A string is passed as input. The program must print the count of vowels. Fill in the lines to implement the function countVowels.
Boundary Condition(s):
1 <= Length of String <= 1000
Input Format:
The first line contains N.
The next N lines contain a string in each line.
Output Format:
The first N lines contain the strings in sorted order.
Example Input/Output 1:
Input:
hello
Output:
2
Example Input/Output 2:
Input:
editable
Output:
4
#include <stdio.h>
int isVowel(char c){
    return c=='a' || c=='e'|| c=='i' || c=='o' || c=='u';
}
int countVowels(char s[1001]){
    int c=0;
    for(int i=0;i<strlen(s);i++){
        if(isVowel(tolower(s[i])))
        c++;
    }
    return c;
}
int main()
{
    char str[1001];
    scanf("%s", str);
    printf("%d", countVowels(str));
}
