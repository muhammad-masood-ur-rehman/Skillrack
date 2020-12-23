Even Position Characters in Reverse Order
A string S is passed as input. The program must print the characters present at the even positions of the string in reverse order.
Boundary Condition(s):
2 <= Length of String <= 1000
Input Format:
The first line contains the string S.
Output Format:
The first line contains the characters at even positions in reverse order.
Example Input/Output 1:
Input:
independent
Output:
ndeen
Example Input/Output 2:
Input:
computer
Output:
rtpo
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{

string s;
cin >> s;

int n = s.length();
if(n%2 == 0)
{
for(int i=n-1;i>=0;i-=2)
{
    cout << s[i];
}
}
else
{
    for(int i=n-2;i>=0;i-=2)
    {
        cout << s[i];
    }
}
}
