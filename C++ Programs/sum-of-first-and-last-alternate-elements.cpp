Sum Of First and Last Alternate Elements
Given an integer array of size N, print the sum of first and last number, second first and second last number and so on.
Note:N is always even.
Boundary Condition:
1<= N <= 9999
Input Format:
The first line contains the size of the array N
The second line contains N integers separated by space.
Output Format:
The first line contains the output as specified.
Example Input/Output 1:
Input:
6
2 9 1 5 3 2
Output:
4 12 6
Example Input/Output 2:
Input:
10
97 94 66 99 17 78 70 44 67 86
Output:
183 161 110 169 95
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{
    int n;
    cin >> n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin >> a[i];
    }
    int x = n/2;
    int ans[n/2];
    int k = n-1;
    for(int i=0;i<x;i++)
    {
        ans[i] = a[i] + a[k];
        k--;
    }
    for(int i=0;i<x;i++)
    {
        cout << ans[i] << " ";
    }

}
