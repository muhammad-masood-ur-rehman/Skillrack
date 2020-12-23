Odd length string diagonal pattern [ZOHO]
Given a string S of odd length L, the program must print it twice as diagonals with the middle letter being the point of intersection.
Input Format:
The first line contains the value of S.
Boundary Conditions:
The length of the String S is from 3 to 20.
1 <= L (Length of S) <= 20
Output Format:
L lines printing the desired pattern.

Example Input/Output 1:
Input:
PROGRAM
Output:
P     M
 R   A
  O R
   G
  O R
 R   A
P     M
Example Input/Output 2:
Input:
CABLE
Output:
C   E
 A L
  B
 A L
C   E
#include<stdio.h>
#include <stdlib.h>

int main()
{
 char String[1000];
 scanf("%s",String);
 int len = strlen(String);
 
 for(int ele=0;ele<len;ele++)
 { 
 int temp=len-ele-1;
 for(int foo=0;foo<len;foo++)
 { 
 if(ele==foo)
 printf("%c",String[foo]);
 else if(foo==temp)
 printf("%c",String[foo]);
 else
 printf(" ");
 
 }
 printf("\n");
 }

}
