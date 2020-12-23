Interchange largest and smallest values
Given N distinct integer values, the program must swap the position of the largest and smallest integer values.
Input Format:
The first line will contain the value of N
The second line will contain N integer values separated by one or more spaces.
Output Format:
The first line will contain the N integer values (with the largest and smallest integer values swapped) separated by a space.
Constraints:
2 <= N <= 25
Example Input/Output 1:
Input:
2
50 100
Output:
100 50
Example Input/Output 2:
Input:
10
3 6 10 21 90 4 9001 89 43 333
Output:
9001 6 10 21 90 4 3 89 43 333
#include<stdio.h>
void main()
{
    int a[10],i,n,min,max,mi,mx,temp;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    min=0;
    max=0;
    for(i=0;i<n;i++){
        if(a[i]<min){ 
            min=a[i];
            mi=i;
        }
        if(a[i]>max){
            max=a[i];
            mx=i;
        }
    }
    temp=a[mi];
    a[mi]=a[mx];
    a[mx]=temp;
    for(i=0;i<n;i++)
    printf("%d ",a[i]);
    printf("\n");
}
