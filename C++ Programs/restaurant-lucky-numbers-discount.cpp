Restaurant - Lucky Numbers Discount
Every day in a restaurant two numbers X and Y are considered lucky numbers.
If the bill amount B is divisible by X, then X% discount is offered.
If the bill amount B is divisible by Y, then Y% discount is offered.
If the bill amount B is divisible by both X and Y, then no amount is to be paid.
The program must accept X, Y and B and print the amount to be paid as the output (precision is upto 3 decimal places)
Input Format:
The first line contains B The second line contains X The third line contains Y
Output Format:
The first line contains the amount to be paid finally after discount.
Boundary Conditions:
1 <= X,Y <= 50
20 <= B <= 100000
Example Input/Output 1:
Input:
500
20
50
Output:
0.000
Example Input/Output 2:
Input:
100
9
10
Output:
90.000
m,b,n=int(input()),int(input()),int(input())
if m%b==0 and m%n==0:
    print("0.000")
elif m%n==0:
    print("%.3f"%(m-m*(n/100)))
elif m%b==0:
    print("%.3f"%(m-m*(b/100)))
else:

    print("%.3f"%(m))
#include <iostream>
#include<iomanip>
using namespace std;
int main(int argc, char** argv)
{
int b,x,y;         //  b as bill number
float d;
cin>>b>>x>>y;
if(b%x==0 && b%y==0)
d=0;
else if(b%x==0)
d=b-(b*x*.01);
else if(b%y==0)
d=b-(b*y*.01);
else
d=b;
cout<<fixed<<setprecision(3)<<d;
}
