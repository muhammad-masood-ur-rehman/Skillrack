Find the count of distinct numbers
A set of numbers will be passed as input. The program has to print the count of distinct numbers in it.
Input Format:
The first line contains the set of numbers separated by a space.
Output Format:
The first line contains the count of distinct numbers.
Example Input/Output 1:
Input:
10 20 30 50 20 32 50
Output:
5
Explanation:
Out of 7 numbers, 20, 50 are repeated once.
Hence distinct count = 7-2 = 5
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int arr[10000000]={0};
    
    int count=0;
    
    int num;
    while(scanf("%d",&num)==1){
        if(!arr[num])count++;
        arr[num]=1;
    }
    printf("%d",count);

}
