C - Heap - ExtractMax
An array of N integers is passed as input. Fill in the missing lines of code to implement the extractMax function to sort in descending order and print the elements using heap sort. The heap is built on array starting from index 0. The left and right child of an element at index is obtained from the index (2*i+1) and (2*i+2) respectively.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains N integers sorted in descending order separated by a space.
Example Input/Output 1:
Input:
6
2 1 7 6 2 12
Output:
12 7 6 2 2 1
Example Input/Output 2:
Input:
8
67 38 20 73 16 93 76 77
Output:
93 77 76 73 67 38 20 16
Max Execution Time Limit: 5000 millisecs
#include<stdio.h>
#include "heap.h"
int extractMax(int ar[],int *size){
    if(*size==0){
        *size=*size-1;
        return ar[0];
    }
    int n=ar[0];
    ar[0]=ar[*size-1];
    *size=*size-1;
    buildMaxHeap(ar,*size,0);
    return n;
}
int main()
{
    int size, index;
    scanf("%d", &size);
    int heapArray[size];
    for(index=0; index<=size-1; index++){
        scanf("%d", &heapArray[index]);
    }
    for(index = size/2-1; index >= 0; index--)
    {
        buildMaxHeap(heapArray, size, index);
    }
    while(size>=1){
        printf("%d ", extractMax(heapArray, &size));
    }
    return 0;
}
