Solve Equations - 001
Given two equations EQN1 and EQN2 containing the values of x co-efficient, y co-efficient and the resulting constant, the program must print the value of x and y separated by a space.
Input Format:
The first line contains the equation EQN1.
The second line contains the equation EQN2.
Output Format:
The first line contains the value of x and y separated by a space.
Boundary Conditions:
1 <= Co-efficient values <= 1000
Example Input/Output 1:
Input:
5x+2y=14
-4y+3x=-2
Output:
2 2
Example Input/Output 2:
Input:
4Y-5X=17
3X+4Y=9
Output:
-1 3
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int a1,b1,c1,a2,b2,c2,temp,a,b,x,y,z;
    char x1,y1,x2,y2;
    scanf("%d%c%d%c=%d",&a1,&x1,&b1,&y1,&c1);
    scanf("%d%c%d%c=%d",&a2,&x2,&b2,&y2,&c2);
    if(x1!='x'&& x1!='X')
    {
        temp=a1;
        a1=b1;
        b1=temp;
    }
    if(x2!='x'&&x2!='X')
    {
        temp=a2;
        a2=b2;
        b2=temp;
    }
 
    a=((c1*b2)-(b1*c2))/((a1*b2)-(b1*a2));
    b=((a1*c2)-(c1*a2))/((a1*b2)-(b1*a2));
        printf("%d %d",a,b);
    
}
