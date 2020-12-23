Replace Middle Character(s) with *
The program must accept a string S as the input. The program must replace the middle character with * in the string S if the length of the string is odd. Else the program must replace the 2 middle characters with * in the string S. Then the program must print the modified string S as the output. 
Top 10 frequently asked HR interview questions
Example Input/Output 1:
Input:
SkillRack
Output:
Skil*Rack
Explanation:
Here the length of the string skillrack is 9, which is odd.
After replacing the middle character with *, the string becomes Skil*Rack.
Hence the output is Skil*Rack
Example Input/Output 2:
Input:
abc@1234
Output:
abc**234
s=input().strip();d=len(s)//2
print(s[0:d]+'*'+s[d+1:]) if len(s)%2==1 else print(s[0:d-1]+'**'+s[d+1:])
#include<stdio.h>
#include <stdlib.h>

int main()
{
char input[1001];
int len;
scanf("%s",input);
len=strlen(input);
input[len/2]='*';
if(len%2==0)
input[len/2-1]='*';
printf("%s",input);
}
