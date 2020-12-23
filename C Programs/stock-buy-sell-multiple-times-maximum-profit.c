Stock Buy & Sell Multiple Times - Maximum Profit
Example Input/Output 1:
Input:
10 5 8 10 12 9 6 14 21 15 10
Output:
22
int main()
{
    int n;
    scanf("%d",&n);
    
    int arr[n];
    for(int i=0;i<n;++i){
        scanf("%d",&arr[i]);
    }
    int maxProfit=0;
    for(int i=1;i<n;++i){
        if(arr[i]-arr[i-1] >0)maxProfit+=(arr[i]-arr[i-1]);
    }
    printf("%d",maxProfit);
}
