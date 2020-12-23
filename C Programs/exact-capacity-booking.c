Exact Capacity Booking
Fed up of overbooking in airlines industry, the government has ordered that airlines cannot book more than the capacity C of an aeroplane. To optimize their revenue, the airlines must confirm booking exactly for C passengers only. The ticket may be booked for just a single passenger or for a group of passengers ranging from 2 to N. (Like 2 tickers for a couple going on a honey moon or 4 tickets for a family of husband, wife and two kids).
Given the capacity C and N, print the number of ways W to fill the C seats using ticket bookings with single passengers or group booking count of 2 to N.
Input Format:
The first line contains the values of C.
The second line contains the values of N.
Output Format:
The first line contains the number of ways W.
Boundary Conditions:
1 <= C <= 500
2 <= N <= 10
Example Input/Output 1:
Input:
5
4
Output:
6
Explanation:
The ways to fill 5 seats using booking count of 1,2,3,4 are (1,1,1,1,1) (1,1,1,2) (1,2,2) (1,1,3) (1,4) (2,3)
Please note that 1,1,3 is same as the combination of 1,3,1 or 3,1,1 and hence not counted as additional ways.
#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
 int i,j,n,m;
 cin>>n>>m;
 int a[n+1] = {0};
 a[0] = 1;
 for(i=1;i<m+1;i++)
  for(j=i;j<n+1;j++)
    a[j] += a[j-i];
  cout<<a[n];
}
