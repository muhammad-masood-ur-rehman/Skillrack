Matrix Maximum Column Sum
An integer matrix of size N*N is given as input. The program must print the maximum column-wise sum of the matrix.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains the value N.
The next N lines contain N elements each separated by space(s).
Output Format:
The first line contains the maximum column sum.
Example Input/Output 1:
Input:
3
1 2 3
4 5 6
7 8 9
Output:
18
Example Input/Output 2:
Input:
6
7 9 8 10 8 5
4 1 8 10 10 3
5 10 5 6 6 4
5 5 7 4 4 3
5 10 10 7 5 7
5 1 4 7 1 1
Output:
44
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
int sum = 0, max = 0 ;
for(int j=0;j<n;j++)
{   
    sum = 0;
    for(int i=0;i<n;i++)
    {
        sum += a[i][j];
    }
    if(sum > max)
    {
        max = sum;
    }
}
cout << max;
}
