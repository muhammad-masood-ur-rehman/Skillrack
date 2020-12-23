Rotated Triangle Pattern
Rotated Triangle Pattern
Given an integer N, print the pattern as given in Example Input/Output section.
Note: N is always an odd number.
Boundary Condition(s):
1 <= N <= 9999
Input Format:
The first line contains N.
Output Format:
The first N lines contain the desired pattern.
Example Input/Output 1:
Input:
7
Output:
1
2 8
3 9 13
4 10 14 16
5 11 15
6 12
7
Example Input/Output 2:
Input:
5
Output:
1
2 6
3 7 9
4 8
5
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{

int n,count = 1;
cin >> n;
int l=0,m=n;
int g = n;
int a[n][n] = {0};

for(int j=0;j<n;j++)
{
    for(int i=l;i<m;i++)
    {
        a[i][j] = count;
        count ++;
    }
    l++;
    m--;
}

for(int i=0;i<n/2+1;i++)
{
    for(int j=0;j<=i;j++)
    {
        cout << a[i][j] << " ";
    }
    cout << endl;
}

for(int i=n/2+1;i<n;i++)
{
    for(int j = 0;j < g; j++)
    {
        if(a[i][j] != 0)
        cout << a[i][j] << " ";
    }
    cout << endl;
    g--;
}

}
