Reversed Sum of Pairs
An array of N integers is passed as input. The program must print the sum of every two consecutive elements in the array from last.
Boundary Condition(s):
1 <= N <= 1000
Input:
4
10 50 30 60
output:
90 60
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int i;
    for(i=n-2;i>=0;i-=2){
        printf("%d ",arr[i]+arr[i+1]);
    }
    if(i==-1){
        printf("%d",arr[0]);
    }
}
