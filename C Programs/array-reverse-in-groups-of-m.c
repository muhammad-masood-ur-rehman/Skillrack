Array Reverse In Groups of M
An array of N integers is passed as the input to the program and the program must reverse the elements in groups of size M.
If the last group size is less than M, then do not reverse the last group.
Input Format:
The first line contains N.
The second line contains N integer values each separated by a space.
Output Format:
The first line contains reversed values of N integers in groups of M separated by a space.
Boundary Conditions:
1 <= N <= 1000
1 <= M <= N
Example Input/Output 1:
Input:
5
10 22 33 45 600
2
Output:
22 10 45 33 600
Example Input/Output 2:
Input:
5
10 22 33 45 600
3
Output:
33 22 10 45 600
Example Input/Output 3:
Input:
6
10 22 33 45 600 514
3
Output:
33 22 10 514 600 45
#include<stdio.h>

int* reverse(int* arr, int length, int M){
    int left=0,right=M-1;
    while(right<length){
        int i=left,j=right;
        while(i<j){
            int t=arr[i];
            arr[i]=arr[j];
            arr[j]=t;
            i++;j--;
        }
        left+=M;
        right+=M;
    }
    return arr;
}
int main()
{
    int N,M;
    scanf("%d",&N);
    int arr[N];
    int index;
    for(index=0; index < N; index++)
    {
        scanf("%d",&arr[index]);
    }
    scanf("%d",&M);

    reverse(arr,N,M);

    for(index=0; index < N; index++)
    {
        printf("%d ",arr[index]);
    }
    return 0;
}
