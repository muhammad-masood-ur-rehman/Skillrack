Isolate Interlaced Strings
Two string values S1 and S2 are interlaced and passed as a single input string S. Given L1 which is the length of S1, print S1 and S2 as the output.
Input Format:
The first line contains S.
The second line contains L1.
Output Format:
The first line contains S1.
The second line contains S2.
Boundary Conditions:
4 <= LENGTH(S) <= 100
1 <= LENGTH(S1) <= 99
1 <= LENGTH(S2) <= 99
Example Input/Output 1:
Input:
LBARZIYSK
4
Output:
LAZY
BRISK
#include<iostream>
#include<string>
using namespace std;
 
int main()
{
    string inp,s1="",s2="";
    cin>>inp;
    int l,l1,l2,i;
    l = inp.length();
    cin>>l1;
    l2 = inp.length() - l1;
    for(i=0; i<l;)
    {
        if(s1.length() < l1)
        {
            s1 += inp[i];
            i++;
        }
        if(s2.length() < l2)
        {
            s2 += inp[i];
            i++;
        }
    }
    cout<<s1<<endl<<s2;
    return 0;
}
