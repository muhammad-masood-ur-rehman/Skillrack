Three Strings
Three Strings: Given N string values, the program must print 3 string values as the output as described in the Example Input/Output section.
Input format: The first line will contain N denoting the number of string values. Next N lines will contain the N string values.
Output format: Three lines containing string values as described in the Example Input/Output section.
Example Input/Output 1:
Input:
3
JOHN
JOHNY
JANARDHAN
Output:
JJOJAN
OHHARD
NNYHAN
Example Input/Output 2:
Input:
4
JOHN
JOHNY
JANARDHAN
MIKESPENCER
Output:
JJOJANMIKE
OHHARDSPE
NNYHANNCER
#include <iostream>
#include<string>
using namespace std;

int main(int argc, char** argv)
{
int n,i,j;
cin>>n;
string s,a,b,c;
for(i=0;i<n;i++)
{
    cin>>s;
    a+=s.substr(0,i+1);
    b+=s.substr(i+1,s.length()-2*(i+1));
    c+=s.substr(s.length()-(i+1));
}
cout<<a<<"\n"<<b<<"\n"<<c;

}
