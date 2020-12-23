Second smallest number
Given a set of elements, write an algorithm and the subsequent ‘C’ program to determine the second smallest element in it.
Input Format
Number of elements in 'n'
Element-1
Element-2
...
Element-n

Output Format
Second smallest element in the set
Input for the problem
Get the n elements
Output for the problem
Second smallest element in the set
#include <stdio.h>
int main()
{ 
    int arr[20];
    int n;
    scanf("%d",&n);
    for(int i = 0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    int i, first=32766, second=32766;
    for (i = 0; i < n ; i ++) 
    {     
        if (arr[i] < first)  
        {        
            second = first;  
            first = arr[i];    
        }     
        else if (arr[i] < second && arr[i] != first) 
          second = arr[i];  
    }
    printf("%d",second);
    return 0;
}
