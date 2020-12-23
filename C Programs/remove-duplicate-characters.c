Remove Duplicate Characters
The program must accept a string S as the input. The program must remove the duplicate characters in the string S and then the program must print the modified string as the output. 
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains the string S.
Output Format:
The first line contains a list of character(s).
Example Input/Output 1:
Input:
blackjaacks
Output:
bljs
Explanation:
In the string blackjaacks, the characters a, c, k occurred more than one time. So remove the characters from the string blackjaacks. Now the string becomes bljs.
Hence the output is bljs
Example Input/Output 2:
Input:
rainbow
Output:
rainbow
C:
#include<stdio.h>
#include <stdlib.h>
int main()
{
    char strin[100];
    scanf("%s",strin);
    
    int arr[256]={0};
    for(int ele=0;ele<strlen(strin);ele++)
	arr[strin[ele]]++;
	
    for(int ele=0;ele<strlen(strin);ele++){
        if(arr[strin[ele]]==1){
            printf("%c",strin[ele]);
            arr[strin[ele]]=0;
        }
    }
}
Python:
s=input().strip()
for i in s:
    if s.count(i)>1:
        s=s.replace(i,'')
print(s)
