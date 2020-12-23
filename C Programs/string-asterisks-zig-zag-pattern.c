String & Asterisks Zig-Zag Pattern
The program must accept a string S and an integer N as the input. The program must form a character matrix of size NxN with the asterisks (*). Then the program must modify the matrix based on the following conditions.
- Replace the last asterisk in the first row of the matrix with the first character in the string S.
- Replace the first two asterisks in the second row of the matrix with the next two characters in the string S.
- Replace the last three asterisks in the third row of the matrix with the next three characters in the string S.
Similarly, the program must replace the asterisks with the characters in the string S for all the rows of the matrix in the zig-zag fashion. If there are no more characters in the string S to replace the asterisks, then the asterisks are replaced with the hash symbols (#). Finally, the program must print the modified matrix as the output.
Boundary Condition(s):
1 <= Length of S <= 1000
2 <= N <= 50
Input Format:
The first line contains S.
The second line contains N.
Output Format:
The first N lines, each containing N characters.
Example Input/Output 1:
Input:
eat
4
Output:
***e
at**
*###
####
Explanation:
Here N = 4, so the 4x4 character matrix is formed with the asterisks (*).
****
****
****
****
After replacing the last asterisk in the first row of the matrix with e (the first character in S), the matrix becomes
***e
****
****
After replacing the first two asterisks in the second row of the matrix with a and t (the next two characters in S), the matrix becomes
***e
at**
****
****
There are no more characters in the string S to replace the asterisks in the third row of the matrix. So the last three asterisks in the third row are replaced with the hash symbols (#).
***e
at**
*###
****
There are no more characters in the string S to replace the asterisks in the fourth row of the matrix. So the first four asterisks in the fourth row are replaced with the hash symbols (#).
***e
at**
*###
####
Example Input/Output 2:
Input:
abcdefghijklmnopqrst
5
Output:
****a
bc***
**def
ghij*
klmno
Example Input/Output 3:
Input:
abcDEfG
7
Output:
******a
bc*****
****DEf
G###***
**#####
######*
#######
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char stringx[1000];
    int num;
    scanf("%s\n%d",stringx,&num);
    
    int l=strlen(stringx);
    int index=0;
    for(int ele=0;ele<num;++ele){
        for(int foo=0;foo<num;++foo){
            if(ele%2){
                printf("%c",foo>ele?'*':(index>=l ? '#':stringx[index++]));
            }
            else{
                printf("%c",foo< num-ele-1 ?'*':(index>=l?'#':stringx[index++]));
            }
        }
        printf("\n");
    }

}
