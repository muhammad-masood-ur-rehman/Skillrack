First N Common Characters
Two string values S1, S2 are passed as the input. The program must print first N characters present in S1 which are also present in S2.
Input Format:
The first line contains S1.
The second line contains S2.
The third line contains N.
Output Format:
The first line contains the N characters present in S1 which are also present in S2.
Boundary Conditions:
2 <= N <= 10

2 <= Length of S1, S2 <= 1000
Example Input/Output 1:
Input:
abcbde
cdefghbb
3
Output:
bcd
Note: b occurs twice in common but must be printed only once.
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{
string a,b;
cin >> a >> b;
int c[26]={0},d[26]={0},n;
cin >> n;
for(int i=0;i<a.length();i++)
    c[a[i]-'a'] = 1;

for(int i=0;i<b.length();i++)
    d[b[i]-'a'] = 1;
 
 
/*
for(int i=0;i<26;i++)
cout << c[i] << " ";
cout << endl;
for(int i=0;i<26;i++)
cout << d[i] << " ";
cout << endl;
*/

int count =0;

for(int i=0;i<a.length();i++)
{
    if( count <n)
    {
        int temp = a[i]-'a';
        if(c[temp] == d[temp])
        {
            count++;
            c[temp]=0;
            cout << a[i];
        }
    }

}


}
