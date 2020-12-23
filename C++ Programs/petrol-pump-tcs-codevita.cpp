Petrol Pump – TCS CodeVita
A big group of students, starting a long journey on a different set of vehicles need to fill petrol in their vehicles.
As a group leader, you are required to minimize the time they spend at the petrol pump to start the journey at the earliest. You will be given the quantity of petrol (in litres) that can be filed in each vehicle.
There are two petrol vending machines at the petrol pump. You need to arrange the vehicles in such a way that that they take the shortest possible time to fill all the vehicles and provide the time taken in seconds as output.
Machine vends petrol @ 1litre / second. Assume that there is no time lost between switching vehicles to start filling petrol.
Constraints:
1 <= Number of vehicles < 50
0 <= Quantity of petrol required in any vehicle <= 200
Input Format:
First-line will provide the quantity of petrol (separated by space) that can be filled in each vehicle.
Output:
Shortest possible time to fill petrol in all vehicles.
Explanation:
Example 1:
Input:
1 2 3 4 5 10 11 3 6 16
Output:
31
Explanation:
First Petrol vending machine will cater to vehicles taking - 16, 6, 4, 3, 2 litres of petrol (Total 31 sec)
The second machine will cater to vehicles taking -11, 10, 5, 3, 1 litres of petrol (Total 30 sec)
Example 2:
Input:
25 30 35 20 90 110 45 70 80 12 30 35 85
Output:
335
Explanation:
First Petrol vending machine will cater to vehicle taking - 80, 45, 35, 30, 25, 12, 85, 20 litres of petrol.
The second machine will cater to vehicles taking - 90, 70, 35, 30, 110 litres of petrol. Since the second machine will take more time, the total time to fill petrol in all vehicles will be 335 seconds.
#include<bits/stdc++.h>
using namespace std;
int maxi=INT_MAX;
int maxx(int a,int b)
{
	return (a>b)?a:b;
}
void calTime(int total,int sum,int i,vector<int> v1)
{
	
	if(maxx(sum,total-sum)<maxi)
	{
		maxi=maxx(sum,total-sum);
	}
	if(v1[i])
	 return;
	calTime(total,sum+v1[i],i+1,v1);
	calTime(total,sum,i+1,v1);
	return;
}
int main()
{
	int n,i=1,sum=0;
	string s;
	vector<int>v1;
	getline(cin,s,'\n');
	stringstream ss(s);
	while(ss>>n)
	{
		sum+=n;
		v1.push_back(n);
	}
	calTime(sum,0,0,v1);
	cout<<maxi;
}
#include <stdio.h>
int main(void) {
    int n=0, x, i, j, s = 0;
    int a[51];
    while((scanf("%d",&x))!=-1)
    {
        a[n++]=x;
        s += x;
    }
    int d[n+1][s+1];
    for(i=0 ; i<=n ; ++i)
        d[i][0] = 1;
    for(i=1 ; i<=s ; ++i)
        d[0][i] = 0;

    for(i=1 ; i<=n ; ++i)
        for(j=1 ; j<=s ; ++j)
        {
            d[i][j] = d[i-1][j];

            if(a[i-1] <= j)
                d[i][j] = d[i][j] | d[i-1][j - a[i-1]];
        }
    int an = s;
    for(i=s/2 ; i>=0 ; --i)
        if(d[n][i])
        {
            an = s - i;
            break;
        }
    printf("%d",an);
 return 0;
}
