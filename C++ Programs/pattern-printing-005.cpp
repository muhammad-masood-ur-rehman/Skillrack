Pattern Printing - 005
Given an integer N as the input, the program must print 2N lines pattern output as described in the Example Input/Output given below.
Input Format:
The first line contains N.
Output Format:
2N lines of the pattern.
Boundary Conditions:
2 <= N <= 100
Example Input/Output 1:
Input:
4
Output:
1
22
333
4444
4444
333
22
1
Example Input/Output 2:
Input:
10
Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999
10101010101010101010
10101010101010101010
999999999
88888888
7777777
666666
55555
4444
333
22
1
#include <stdio.h>

int main() {
    int n,i,j;
    scanf("%d",&n);
    for(i=1;i<=2*n;i++){
        if(i<=n)
        for(j=0;j<i;j++)
        printf("%d",i);
        else
        for(j=0;j<2*n-i+1;j++)
        printf("%d",2*n-i+1);
        printf("\n");
    }
}
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
int n,i,j;
cin>>n;
for(i=1;i<=n;i++)
{
    for(j=0;j<i;j++)
    {
        cout<<i;
    }
    cout<<"\n";
}
for(i=n;i>=0;i--)
{
    for(j=0;j<i;j++)
    {
        cout<<i;
    }
cout<<"\n";
}
}
