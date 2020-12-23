Concatenate Strings Alphabetically
Two string values S1 and S2 are passed as the input. The program must concatenate them depending on which string comes first in the alphabetical order.
Example 1:
Input:
apple
orange
Output:
appleorange
Example 2:
Input:
zoo
tiger
Output:
tigerzoo
#include<stdio.h>
#include <stdlib.h>

int main()
{
char first[1000],second[1000];
scanf(“%s%s”,first,second);
if(first[0]>second[0])
printf(“%s%s”,second,first);
else
printf(“%s%s”,first,second);

}
