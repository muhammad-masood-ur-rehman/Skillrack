Character Between Two Vowels
Given a string S, Print only the characters which are surrounded by vowels on both sides, if no character matches the condition print -1.
Input Format:
The first line contains the value of string S
Output Format
The first line contains the characters which are surrounded by vowels on both sides if not print -1
Boundary Condition:
3 <= length of the S <= 100
Example Input/Output 1:
Input:
acceleration
Output:
let
Example Input/Output 2:
Input:
knowledge
Output:
-1
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{

string a;
cin >> a;
int n = a.length();
int flag = 0;
for(int i=1;i<n-1;i++)
{
    if((a[i-1]=='a' || a[i-1]=='e' || a[i-1]=='i' || a[i-1]=='o' || a[i-1]=='u') && (a[i+1]=='a' || a[i+1]=='e' || a[i+1]=='o' || a[i+1]=='i' || a[i+1]=='u'))
    {
        cout << a[i] ;
        flag = 1;
    }
}

if(flag == 0)
{
  cout << "-1";    
}

}
