C - Find the sum of the largest and smallest number in an Array.
N numbers are passed as input to the program. The program must find the sum of the largest and smallest number in the Array.
Input Format:
The first line will contain the value of N.
Next N lines will contain the value of the N integers
Output Format:
The first line will contain the sum of the largest and smallest integers in the Array.
Boundary Conditions:
2 <= N <= 15
1 <= The values in the array <= 999999
Example Input/Output 1:
Input:
5
100
200
555
234
800
Output:
900
Explanation:
Largest number is 800 and smallest is 100. So their sum 900 is printed as the output.
Example Input/Output 2:
Input:
3
30
30
30
Output:
60
#include<stdio.h>
#include <stdlib.h>
int sumOfLargestAndSmallest(int arr[],int n){
    int max=arr[0],min=arr[0];
    for(int ele=1;ele<n;ele++){
        if(arr[ele]>max)
        max=arr[ele];
        if(arr[ele]<min)
        min=arr[ele];
    }
    return max+min;
}
int main()
{
    int N;
    scanf("%d",&N);
    int arr[N];
    int ctr=0;
    for(; ctr < N; ctr++)
    {
        scanf("%d",&arr[ctr]);
    }
    printf("%d",sumOfLargestAndSmallest(arr, N));
    return 0;
}
