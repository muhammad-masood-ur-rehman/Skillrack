Merge Two Sorted Arrays
Given two sorted arrays A1 and A2 with size S1 and S2 respectively, merge the two array elements in sorted order and print the sorted elements as the output.
Input Format:
The first line contains S1 and S2 separated by space.
The second line contains elements of A1 separated by a space.
The third line contains elements of A2 separated by a space.
Output Format:
The first line contains S1+S2 elements in sorted order
Boundary Conditions:
1 <= S1, S2 <= 1000
Example Input/Output 1:
Input:
3 4
1 5 7
2 3 4 5
Output:
1 2 3 4 5 5 7
Example Input/Output 2:
Input:
4 4
6 7 9 12
3 8 15 18
 
Output:
3 6 7 8 9 12 15 18
#include <stdio.h>
#include<stdlib.h>
int merge_arrays(int arr1[], int arr2[], int arr3[], int m, int n){
    int i,j;
    for(i = 0; i < m; i++){
        arr3[i] = arr1[i];
    }
    for(i = m, j = 0 ; i < m + n; i++, j++){
        arr3[i] = arr2[j];
    }
}

int main(){
    int n,m;
    scanf("%d",&m);
    scanf("%d",&n);
    int arr1[m],arr2[n];
    int arr3[m+n];
    int i;
    for(i = 0; i<m;i++){
        scanf("%d",&arr1[i]);
    }
    for(i = 0;i<n;i++){
        scanf("%d",&arr2[i]);
    }
    merge_arrays(arr1,arr2,arr3,m,n);
    for(i = 0; i < m+n-1; i++){
        for(int j = 0; j < m+n-i-1; j++){
            if(arr3[j] > arr3[j + 1]){
                int temp = arr3[j];
                arr3[j ] = arr3[j + 1];
                arr3[j + 1] = temp;
            }
        }
    }
    for(i = 0; i < n + m; i++){
        printf("%d ",arr3[i]);
    }
    printf("\n");
    return 0;
}
