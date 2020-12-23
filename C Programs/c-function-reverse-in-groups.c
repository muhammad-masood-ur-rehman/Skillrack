C - Function - Reverse In Groups
Given an array of integers of size N and size of group R as input, the program must reverse and print every R elements in the array. Please fill in the lines of code to define the method reverseInGroups so that the program runs successfully.
Boundary Condition(s):
1 <= N, R <= 100
Input Format:
The first line contains the value of N and R separated by a space.
The second line contains N elements separated by space(s).
Output Format:
The first line contains N elements separated by space.
Example Input/Output 1:
Input:
10 4
10 20 30 40 50 60 70 80 90 100
Output:
40 30 20 10 80 70 60 50 90 100
Explanation:
Reverse the first 4 elments -> 40 30 20 10
Reverse the next 4 elements -> 80 70 60 50
At last only 2 elements left which less than 4 so keep as it is -> 90 100
Hence the output is 40 30 20 10 80 70 60 50 90 100
Example Input/Output 2:
Input:
7 8
2 4 6 8 10 12 14
Output:
2 4 6 8 10 12 14
Explanation:
The array has only 7 elements which is less than 8 so keep as it is -> 2 4 6 8 10 12 14
Hence the output is 2 4 6 8 10 12 14
#include <stdio.h>
void reverseInGroups(int arr[], int N, int R) 
{
  if(R<=N) 
  {
    int start=0,end=R-1; 
    while(start<end) 
    {
      int t=arr[start];
      arr[start]=arr[end]; 
      arr[end]=t;  
      start++; 
      end--;
    } 
  } 
}
void main()
{
    int N, R, index;
    scanf("%d%d", &N, &R);
    int arr[N];
    for(index=0; index<N; index++)
    {
        scanf("%d", &arr[index]);
    }
    reverseInGroups(arr, N, R);
    for(index=0; index<N; index++)
    {
        printf("%d ", arr[index]);
    }
}
