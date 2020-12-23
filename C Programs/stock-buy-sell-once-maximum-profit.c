Stock Buy & Sell Once - Maximum Profit
Input:
7 50 100 40 60 70 50 80
Output:
50
#include<stdio.h>
#include <stdlib.h>
#define max(x,y) x>y? x: y
#define min(x,y) x<y? x: y
int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    
    for(int i=0;i<n;++i)scanf("%d",&arr[i]);
    
    int maxProfit=0,currentProfit=0,mini=arr[0];
    
    for(int i=1;i<n;++i){
        currentProfit=arr[i]-mini;
        maxProfit=max(currentProfit,maxProfit);
        mini=min(arr[i],mini);
    }
    printf("%d",maxProfit);
}
