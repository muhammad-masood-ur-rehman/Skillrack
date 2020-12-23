Sort In Subsets of Size K
Sort In Subsets of Size K: Given N numbers, the program must sort within subsets of size K. That is every K numbers must be sorted among themselves. (The last subset may not have K numbers in certain cases, but the program must sort them too)
Input Format:
The first line contains N and K separated by space.
The second line contains N numbers separated by space.
Output Format:
The first line contains N numbers sorted in subsets of size K.
Boundary Conditions:
2 <= N <= 9999
Value of a given number is from -99999 to 99999
Example Input/Output 1:
Input:
11 3
880 111 1440 1326 1892 -365 -761 -489 -131 1199 324
Output:
111 880 1440 -365 1326 1892 -761 -489 -131 324 1199
n,k=map(int,input().split())
l=list(map(str,input().split()))
for i in range(n):
    l[i]=int(l[i])
for i in range(n//k):
    l[i*k:(i+1)*k]=sorted(l[i*k:(i+1)*k])
l[((n//k)*k):]=sorted(l[((n//k)*k):])
for i in l:
    print(i,end=" ")
#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char** argv)
{
int i,j,k,l,m,n,count = 0;
cin >> n >> k;
int a[n];
for(i=0;i<n;i++) cin >> a[i];
for(i=0;i<n-(n%k);i++)
{
    if(i%k==0)
    {
        sort(a+i,a+k+i);
        count += k;
    }
}
sort(a+count,a+n);
for(i=0;i<n;i++)
cout << a[i] << " ";

}
