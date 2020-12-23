Infinity Symbol Pattern
Given a matrix M of size N*N as input, the program must print the output as shown in the Example Input/Output section.
Boundary Condition(s):
2 <= N <= 50
Input Format:
The first line contains the value of N.
The next N lines contain N values each separated by space.
Output Format:
The first line contains the desired output as shown in the Example Input/Output section.
Example Input/Output 1:
Input:
3
1 2 3
5 6 7
2 3 4
Output:
1 6 4 7 3 6 2 5 1
Example Input/Output 2:
Input:
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Output:
1 6 11 16 12 8 4 7 10 13 9 5 1
#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
int n;
cin >> n;
int a[n][n];
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
        cin >> a[i][j];
    }
}

for(int i=0;i<n;i++)
{
    cout << a[i][i] << " ";
}

for(int i=n-2;i>=0;i--)
{
    cout << a[i][n-1] << " ";
}

int k = n-2;
for(int i=1;i<n;i++)
{
    cout << a[i][k] << " ";
    k--;
}

for(int i=n-2;i>=0;i--)
{
    cout << a[i][0] << " ";
}
}
