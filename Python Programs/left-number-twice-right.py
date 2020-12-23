Left Number Twice Right
A set of N numbers (separated by one or more spaces) is passed as input to the program. The program must identify the count of numbers C where the number on the left is twice the number on the right.
Boundary Conditions:
3 <= N <= 50
The value of the numbers can be from -99999999 to 99999999
Input Format:
The first line will contain the N numbers separated by one or more spaces.
Output Format:
The first line contains the value of C.
Example Input/Output 1:
Input:
10 20 5 40 15 -2 -30 -1 60
Output:
2
Explanation:
The numbers meeting the criteria are 20, -30
Example Input/Output 2:
Input:
5 90 10 2 5 -4 10 6 5 3
Output:
3
Explanation:
The numbers meeting the criteria are 2, 6, 5
Python:
a,c=[int(i) for i in input().split()],0
for i in range(1,len(a)-1):
    if a[i-1]==2*a[i+1]:
        c+=1
print(c)
l=list(map(int,input().split()));c=0
for i in range(len(l)-1):
  if l[i-1]*2==abs(l[i+1]):c+=1
print(c)
C++:
#include <iostream>
#include<cstdio>
using namespace std;

int main(int argc, char** argv)
{
int c=0,a[100],i,j;
char ch;
for(i=0;;i++)
{
    scanf("%d%c",&a[i],&ch);
    if(ch!=' ')
    break;
}
int n=i;

for(i=0;i<=n;i++)
{
    if(a[i]%2==0)
    {
        for(j=i+1;j<=n;j++)
        {
            if(a[i]/2==a[j])
            {
                c++;
                break;
            }
        }
    }
}
cout<<c;

}
