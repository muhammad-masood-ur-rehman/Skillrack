String Stairs Pattern
The program must accept a string S containing only alphabets as the input. The program must print the string S for (L*2)-1 times (where L is the length of the string S) based on the following conditions.
- In line 1, the program must print L-1 hyphens and the first alphabet in S.
- In line 2, the program must print L-2 hyphens and the first two alphabets in S.
- Similarly, the program prints the first L lines as the output.
- In line L+1, the program must print the string S except the first alphabet.
- In line L+2, the program must print the string S except the first two alphabets.
- Similarly, the program prints the remaining lines as the output.
Boundary Condition(s):
3 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The first (L*2)-1 lines containing the string values based on the given conditions.
Example Input/Output 1:
Input:
receiving
Output:
--------r
-------re
------rec
-----rece
----recei
---receiv
--receivi
-receivin
receiving
eceiving
ceiving
eiving
iving
ving
ing
ng
g
Explanation:
The length of the given string receiving is 9. So the pattern contains (9*2)-1 lines.
In line 1, 8 hyphens and the first alphabet in S are printed.
In line 2, 7 hyphens and the first two alphabets in S are printed.
In line 3, 6 hyphens and the first three alphabets in S are printed.
Similarly, the first 9 lines are printed.
--------r
-------re
------rec
-----rece
----recei
---receiv
--receivi
-receivin
receiving
In line 10, the string S is printed except the first alphabet.
In line 11, the string S is printed except the first two alphabets.
In line 12, the string S is printed except the first three alphabets.
Similarly, the remaining lines are printed.
eceiving
ceiving
eiving
iving
ving
ing
ng
g
Example Input/Output 2:
Input:
ZERO
Output:
---Z
--ZE
-ZER
ZERO
ERO
RO
O
Example Input/Output 3:
Input:
KeyBoard
Output:
-------K
------Ke
-----Key
----KeyB
---KeyBo
--KeyBoa
-KeyBoar
KeyBoard
eyBoard
yBoard
Board
oard
ard
rd
d
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
int ele,foo,num;
char strin[101];
scanf("%strin",strin);
for(ele=0;ele<strlen(strin);ele++)
{
    for(foo=0;foo<strlen(strin)-ele-1;foo++)
    printf("-");
    for(foo=0;foo<=ele;foo++)
    printf("%c",strin[foo]);
    printf("\n");
}
for(ele=1;ele<strlen(strin);ele++)
{
    printf("%strin",&strin[ele]);
    printf("\n");
}
}
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char str[10001];
    scanf("%strin",str);
    
    int length=strlen(str);
    for(int ele=0;ele<(length*2)-1;ele++){
        for(int foo=0;foo<length-ele-1;foo++){
            printf("-");
        }
        int var1,var2;
		if(length-ele-1>=0){
			var1=0;
		}
		else{
			var1=ele%length+1;
		}
		if(length-ele-1>=0){
			var2=ele+1;
		}
		else{
			var2=length;
		}
        for(int foo=var1;foo<var2;foo++){
			printf("%c",str[foo]);
		}
        printf("\n");
    }
    
    return 1;
}
