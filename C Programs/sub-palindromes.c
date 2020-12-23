Sub Palindromes
Given a string S, the program must print the count of sub palindromes(with a minimum length of two characters) in the string S.
Example 1:
Input:
everest
Output:
2
Explanation:
The sub palindromes are eve, ere.
#include<stdio.h>
#include <stdlib.h>

int main()
{
 char str[1000];
 int res=0;
 scanf("%s",str);
 
 for(int i=0;i<strlen(str);i++)
 {
 for(int j=i+1;j<strlen(str);j++)
 {
 if(str[i]==str[j])
 { int count=0;
 for(int k=i,l=j;k<=j,l>=i;k++,l--)//palindrome check
 {
 if(str[k]==str[l])
 count++;//no of common letters
 }
 if(count==(j-i)+1)//check of count with length of that string ex:eve=3
 res++;//if true it is palindrome so increment the count of res. 
 }
 }
 }
 printf("%d",res);

}
