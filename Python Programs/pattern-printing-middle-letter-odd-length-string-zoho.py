Pattern Printing Middle Letter - Odd Length String [ZOHO]
Pattern Printing Middle Letter - Odd Length String [ZOHO]: An odd length string S is passed as the input. The program must print the pattern as described below.Let L be the length of the string and M denote the middle position of the string S. The characters in the string are a(1),...., a(M), .... a(L).
- The first line will contain the middle letter a(M) of S in the extreme right.
- Then in each subsequent line, the letters after the middle letter from a(M+1) to a(L) is appended to the line output.
- After the end of the string a(L) is reached, in each subsequent line, the letters from the beginning to the middle letter, a(1) to a(M-1) are appended to the line output.
Note: Asterisk * will be used to pad in the front so that each line has L characters
Input Format:
The first line will contain S.
Output Format:
L lines as output where L is the length of the string S.
Boundary Conditions:
3 <= L <= 1001
Example Input/Output 1:
Input:
CRY
Output:
**R
*RY
RYC
Example Input/Output 2:
Input:
PROGRAM
Output:
******G
*****GR
****GRA
***GRAM
**GRAMP
*GRAMPR
GRAMPRO
Python:
s=input().strip();k=len(s);x=[];y=len(s)//2;c=0;l=''
for i in range(k):
    x.append(''(k-1));k-=1
    if i<=len(s)//2:l+=s[y];x.append(l);y+=1 
    elif i>len(s)//2 and i<len(s):l+=s[c];x.append(l);c+=1
    print(''.join(x));x=[]
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char s[100],a[100];
    scanf("%s",s);
    int len,mid,k=0;
    len=strlen(s);
    mid=len/2;
    for(int i=mid;i<strlen(s);i++)
    a[k++]=s[i];
    for(int i=0;i<strlen(s);i++)
    a[k++]=s[i];
    for(int i=0;i<strlen(s);i++){
        k=0;
        for(int j=0;j<strlen(s);j++){
            if(j<len-1)
            printf("*");
            if(j>=len-1)
            printf("%c",a[k++]);
        }
        len--;
        printf("\n");
    }
    return 0;

}
