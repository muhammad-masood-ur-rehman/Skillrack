Area of Equilateral Triangle
The program must accept the side S of an equilateral triangle as the input. The program must print the area of the equilateral triangle with the precision up to two decimal places as the output.
Formula: Area of an equilateral triangle = √3/4 × a²
Example Input/Output 1:
Input:
5
Output:
10.83
Explanation:
Here the side S = 5.
The area of the equilateral triangle with the precision up to two decimal places is printed as the output.
So 10.83 is printed.
Example Input/Output 2:
Input:
18
Output:
140.30
Python:
import math as m
num=int(input())
x=pow(num,2)
y=(3/4)*x
print("{:.2f}".format((m.sqrt(y))

C:
#include<stdio.h>
#include<stdlib.h>
#define R (sqrt(3))
int main()
{
long int num;
scanf("%ld",&num);
printf("%.2f",(R*num*num)/4);
}
#include<stdio.h>
#include <math.h>
#define rootofthree (sqrt(3))
int main()
{
long int number;
scanf("%ld",&number);
printf("%.2f",(rootofthree*number*number)/4.0);
}
#include<stdio.h>
#include <stdlib.h>
int main()
{
    int n;
    scanf("%d",&n);
     double area=(sqrt(3)*n*n)/4.0;
     printf("%.2lf",area);
}
C++:
#include <bits/stdc++.h>
 
using namespace std;

int main()
{
double side;
cin>>side;
double area=sqrt(3)/4.0*side*side;
cout<<fixed<<setprecision(2)<<area<<endl;

}
