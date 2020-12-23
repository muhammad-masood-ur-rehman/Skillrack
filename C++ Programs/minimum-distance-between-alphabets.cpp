Minimum Distance Between Alphabets
Minimum Distance Between Alphabets: Given a string S and two alphabets C1 and C2 present in S, find the minimum distance D  between C1 and C2 in S.
Input Format:
The first line will contain S.
The second line will contain C1 and C2 separated by a space.
Output Format:
The first line will contain D.
Boundary Conditions:
2 <= Length of S <= 100
Example Input/Output 1:
Input:
spaceship
c s
Output:
1
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
string s;
cin>>s;
char a,b;
cin>>a;
cin>>b;
int m=s.length(),flag=0,d=0;
for(int i=0;i<s.length();i++)
{
    if(s[i]==a||s[i]==b)
    {
        if(flag==1&&d!=0)
        {
        if(d<m)
        m=d;
        d=0;
        }
        else
        flag=1;
    }
    if(flag==1)
    d++;
}
cout<<m-1;
}
