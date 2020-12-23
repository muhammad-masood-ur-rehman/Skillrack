Decreasing String in Center - Pattern
A string S is passed as the input to the program. The program must print the pattern as shown in the Example Input/Output sections.
Note: The length of the string is always even.
Boundary Condition(s):
1 <= Length of the string <= 100
Input Format:
The first line contains the string S.
Output Format:
The lines contain the pattern as shown in the Example Input/Output sections.
Example Input/Output 1:
Input:
barber
Output:
barber
*baer*
**br**
******
Example Input/Output 2:
Input:
database
Output:
database
*datase*
**dase**
***de***
********
#include<stdio.h>
#include <stdlib.h>
void func(int num){
    while(num--)printf("*");
    return;
}
int main()
{
    char strin[100];
    scanf("%s",strin);
    int strin_length=strlen(strin);
    int temp=strin_length/2;
	int start=strin_length/2;
    for(int ele=0;ele<(strin_length/2)+1;++ele){
        func(ele);
        for(int foo=0;foo<temp;foo++){
            printf("%c",strin[foo]);
        }
        for(int foo=start;foo<strin_length;foo++){
            printf("%c",strin[foo]);
        }
        func(ele);
        temp-=1;
        start+=1;
        printf("\n");
    }

}
