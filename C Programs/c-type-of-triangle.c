C - Type of triangle
The length of three sides of triangle A,B,C will be passed as input. The program must print the type of the triangle.
Input Format:
First line will contain value for A - length of the first side.
Second line will contain value for B - length of the second side.
Third line will contain value for C - length of the third side.
Output Format:
First line will contain the string value which represents the type of the triangle. The value will be one among scalene, isosceles, equilateral.
Please note that the output value is CASE SENSITIVE.

Constraints:
0 < A <= 9999999
0 < B <= 9999999
0 < C <= 9999999

Sample Input/Output:
Example 1:
Input:
5
4
5
Output:
isosceles

Example 2:
Input:
9
9
9
Output:
equilateral

Example 3:
Input:
5
7
4
Output:
scalene
#include<stdio.h>
 
int main()
{
	int side1, side2, side3;
 
  	scanf("%d\n%d\n%d", &side1, &side2, &side3);
  	
  	if(side1 == side2 && side2 == side3)
  	{
  		printf("equilateral");
 	}
 	else if(side1 == side2 || side2 == side3 || side1 == side3)
 	{
 		printf("isosceles");
	}
	else
	{
		printf("scalene");
	}  
 	return 0;
 }
