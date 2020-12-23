Sum of Unique Elements in the Array
The program must accept a positive integer array of size N as the input. The program
must print the sum of unique elements in the array as the output.
Boundary Condition(s):
3 <= N <= 50
1 <= Array Element Value <= 99
Input Format:
The first line contains the value of N.
The sceond line contains N integers separated by space(s).
Output Format:
The first line contains the sum of unique elements in the array.
Example Input/Output 1:
Input:
5
1 2 3 4 2
Output:
8
Explanation:
The unique elements in the array are 1 3 4.
The sum of unique elements in the array is 8.
Hence the output is 8
Example Input/Output 2:
Input:
8
2 3 4 5 2 3 4 5
Output:
0
#include<stdio.h>
#include <stdlib.h>
int main()
{
    int n,i,j,flag,sum=0,cnt;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    
    for(i=0;i<n;i++)
    {
        flag=0;cnt=0;
        for(j=i+1;j<n;j++)
        {
            if(a[i]==a[j])
            {
                flag=1;
                cnt++;
                a[j]=0;
            }
        }
        if(flag==0 && cnt==0)
            sum+=a[i];
    }
    printf("%d",sum);
}
