Price before GST
The amount payable after GST - AP is applied is passed as the input. The GST rate R as percentage is also passed as the input.
The program must print the price P on which the GST was applied, with the precision upto 2 decimal places.
Input Format:
The first line contains AP.
The second line contains R.
Output Format:
The first line contains P.
Boundary Conditions:
1.00 <= AP <= 99999.99
2 <= R <= 40
Example Input/Output 1:
Input:
118
18
Output:
100.00
Example Input/Output 2:
Input:
133.10
10
Output:
121.00
print("%.2f" %((100*float(input()))/(100+int(input()))))
#include<stdio.h>
int main()
{
float s,p;
scanf("%f %f",&s,&p);
printf("%.2f",(s*100)/(100+p));
}
