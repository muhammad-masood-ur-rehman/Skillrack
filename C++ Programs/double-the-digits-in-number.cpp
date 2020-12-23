Double the Digits in Number
Given a positive integer N, the program must print double the value for each of it's digits.
Boundary Condition(s): 1 <= N <=999999999
Example Input/Output 1:
Input: 15
Output: 210
Explanation: 
1*2 = 2 
5*2 = 10
and hence 210 is printed
#include <iostream>
 
using namespace std;
long int reverse(long int n)
{   
    long int ans = 0;
    while(n >0)
    {
        ans = (ans*10) + n%10;
        n/=10;
    }
    return ans;
}
int main(int argc, char** argv)
{

long int n,ans = 0,t;
cin >> n;
long int temp = n;
n = reverse(n);
while(n>0)
{
    t = n%10;
    cout << t*2;
    n/=10;
}

//Handling zeros
int count = 0;
while(temp%10==0)
{
    temp/=10;
    count++;
}

for(int i=0;i<count;i++)
{
    cout << "0";
}
}
