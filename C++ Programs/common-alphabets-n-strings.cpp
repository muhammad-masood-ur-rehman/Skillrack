Common Alphabets N Strings
N string values are passed as input to the program.
Each string will contain only the alphabets a-z in lower case. A given alphabet may be repeated any number of times.
The program must print the count C of the alphabets that are present in all the N string values.
Input Format:
The first line contains N.
Next N lines contain the N string values.
Output Format:
The first line contains C.
Boundary Conditions:
2 <N <500
1 <Length of the string value <1000
Example Input/Output 1:
Input:
3
mnppqqr
ajkmnnm
poormanagement
Output:
2
Explanation :
Only 2 alphabets m and n are present in all the three string values.
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{
int n;
cin >> n;
string a[n],temp;

for(int i=0;i<n;i++)
{
    cin >> a[i];
}

int b[n][26]={0},c;

for(int i=0;i<n;i++)
{
    temp = a[i];
    for(int j=0;j<temp.length();j++)
    {
        c = temp[j]-97;
        b[i][c]++;
    }
}
int flag,count = 0;

for(int i=0;i<26;i++)
{
    flag = 1;
    for(int j=0;j<n;j++)
    {
        if(b[j][i] <= 0)
        {
            flag = 0;
        }
    }
    
    if(flag == 1)
    {
        count++;
    }
}

cout << count;
return 0;
}
