Traverse Square Matrix - Spiral Clockwise
A square matrix of size N*N is provided. The program must traverse the matrix spirally and print the elements in a single line.
Input Format:
The first line contains N.
Next N lines, contain N column values C(i,j) each separated by a space.
Output Format:
The first line contains N*N values separated by a space.
Boundary Conditions:
2 <= N <= 100
0 <= C(i,j) <= 9999
Example Input/Output 1:
Input:
2
1 2
3 4Output:
1 2 4 3
Example Input/Output 2:
Input:
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Example Input/Output 3:
Input:
5
2 7 7 7 9
10 2 4 2 10
2 9 4 9 2
7 15 10 14 10
12 9 15 12 2
Output:
2 7 7 7 9 10 2 10 2 12 15 9 12 7 2 10 2 4 2 9 14 10 15 9 4
#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
int n,i,j,k;
cin>>n;
int arr[n][n];
for(i=0;i<n;i++)
    for(j=0;j<n;j++)
        cin>>arr[i][j];
for(i=n-1,j=0;i>0;i--,j++)
    {
        for(k=j;k<i;k++)
            cout<<arr[j][k]<<" ";
        for(k=j;k<i;k++)
            cout<<arr[k][i]<<" ";
        for(k=i;k>j;k--)
            cout<<arr[i][k]<<" ";
        for(k=i;k>j;k--)
            cout<<arr[k][j]<<" ";
    }
   
    int m=(n-1)/2;
    if(n%2==1)
        cout<<arr[m][m];
}
