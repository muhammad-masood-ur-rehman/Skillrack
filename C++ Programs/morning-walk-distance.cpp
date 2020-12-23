Morning Walk Distance
A man in order to reduce his weight walks along the boundary of a rectangular plot every morning. Depending on his energy level he walks for N rounds on a given day.
Given the length L and breadth B of the rectangular plot along with the number of rounds N, the program must print the total distance D covered in the morning walk.
Note: Do not worry about the units like meters or kilometers.
Input Format:
The first line contains L and B separated by a space.
The second line contains N.
Output Format:
The first line contains D.
Boundary Conditions:
1 <= N <= 100
1 <= L, B <= 999999
Example Input/Output 1:
Input:
10 20
5
Output:
300
n,m=[int(i) for I in input().split()]
z=int(input())

print(2*(n+m)*z)
#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
    int l,b,n;
    cin>>l>>b>>n;
   cout<<2*(l+b)*n;

}
