Matrix Find String Row-wise
A character matrix of size N*N and a string S are given as input.
The program must check if the string is present in the matrix row-wise and print the row number of the rows with the given string in it.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains the value N.
The next N lines contain N characters each separated by space(s).
The N+2th line contains the string S.
Output Format:
The row number values of rows with the given string are printed in each line.
Example Input/Output 1:
Input:
4
s k i l 
k t h e
r t c k 
k t h e
the
Output:
2
4
Example Input/Output 2:
Input:
6
l w r w s g
s k r l l r
k s k i l l
r q e g h u
r t k e w c
s k i l l q
skill
Output:
3
6
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{

int n;
cin >> n;
char a[n][n];
string b;
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
        cin >> a[i][j];
    }
}
cin >> b;
int  k = 0,count = 0;
for(int i=0;i<n;i++)
{
    k = 0;
    count = 0;
    for(int j=0;j<n;j++)
    {
        if(a[i][j] == b[k])
        {
            count++;
            k++;
        }
    }
   //cout << count << endl;
    if(count == b.length())
    {
        cout << i+1 << endl;
    }
}
}
