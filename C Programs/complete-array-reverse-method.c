Complete Array reverse Method
An array of N integers is passed as the input to the program and the program must print the array after reversing it.
Complete the method reverse so that the program can execute successfully.
Input Format:
The first line contains N.
The second line contains N integer values each separated by a space.
Output Format:
The first line contains reversed values of N integers separated by a space.
Boundary Conditions:
1 <= N <= 1000
Example Input/Output 1:
Input:
5
10 22 33 45 600
Output:
600 45 33 22 10
#include<stdio.h>
#include <stdlib.h>

void reverse(int arr[],int length){
    length--;
    for(int i=0;i<length;++i){
        int t=arr[i];
        arr[i]=arr[length];
        arr[length]=t;
        length--;
    }
}
int main()
{
    int N;
    scanf("%d",&N);
    int arr[N];
    int index;

    for(index=0; index < N; index++)
    {
        scanf("%d",&arr[index]);
    }

    reverse(arr, N);

    //Printing the output
    for(index=0; index < N; index++)
    {
        printf("%d ",arr[index]);
    }
}
