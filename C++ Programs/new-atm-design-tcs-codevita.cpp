New ATM Design – TCS CodeVita
Automated Teller Machine (ATM) is an electronic device that enables people to withdraw cash from their bank account. Every ATM has a limit for number of currency notes (say N), it can give at a time.
A bank wants to design an ATM for school students. The unique feature of this ATM would be that it would always give maximum number of currency notes possible, to make the students happy. Available denomination of currency notes in the ATM are 100, 200, 500, 1000
Constraints:
N<100
Input Format:
First Line provides an integer, N
Second Line provides an integer denoting the amount you want to withdraw (in multiples of 100)
Third Line provides an integer denoting the available currency note of Rs 100 in the ATM
Fourth Line provides an integer denoting the available currency note of Rs 200 in the ATM
Fifth Line provides an integer denoting the available currency note of Rs 500 in the ATM
Sixth Line provides an integer denoting the available currency note of Rs 1000 in the ATM
Output:
One line containing the maximum number of currency note possible for the desired withdrawal amount. Output should be 0 (zero) if transaction is not possible, for example if sufficient fund is not available in the ATM.
Time Limit:
1
Explanation:
Example 1:
Input:
10
1300
10
10 
10
10
Output:
10
Explanation:
Here,
7 * 100 + 3 * 200 + 0 * 500 + 0 * 1000 hence maximum possible currency = 10.
Example 2:
Input:
5
1700
1
2
2
2
Output:
3
Explanation:
Here,
0 * 100 + 1 * 200 + 1 * 500 + 1 * 1000 hence maximum possible currency = 3.
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int sum,sum1,sum2,sum3,amount,n,hundred,twohundred,fivehundred,thousand,i,j,k,l,count=0;
	cin>>n;
	cin>>amount;
	cin>>hundred;
	cin>>twohundred;
	cin>>fivehundred;
	cin>>thousand;
	for( i = 0; i <= hundred; i++)
	{
		sum= i*100;
		if(sum == amount && i<=n && i>count)
		count = i;
		if(sum < amount)
		for( j = 0; j<=twohundred; j++)
		{
		sum1=sum+j*200;
		if(sum1 == amount && (i+j) <= n && (j+i)>count)
		count= i + j;
		if(sum1 < amount)
		for(k = 0; k<=fivehundred; k++)
		{
		sum2= sum1 + k*500;
		if(sum2 == amount && (i+j+k)<=n && (i+j+k)>count)
	        count= i + j + k;
		if(sum2 < amount)
		for(l = 0; l<=thousand; l++)
		{
		sum3= sum2+ l*1000;
		if(sum3 == amount && (i+j+k+l)<=n && (i+j+k+l)>count)
		count= i + j + k + l;
		if(sum3 > amount)
		 l= thousand + 1;
		}
		}
		}
	}
	cout<<count;
	return 0;
}
