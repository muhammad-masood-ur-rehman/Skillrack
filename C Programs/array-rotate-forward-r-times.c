Array Rotate Forward - R times
An array of N integers is passed as the input to the program and the program must rotate the elements R times in forward direction.
Input Format:
The first line contains N.
The second line contains N integer values each separated by a space.
The third line contains R.
Output Format:
The first line contains rotated integer values separated by a space.
Boundary Conditions:
1 <= N <= 100
1 <= R <= 10000000
Example Input/Output 1:
Input:
5
1 2 3 4 5
2
Output:
4 5 1 2 3
Example Input/Output 2:
Input:
5
1 2 3 4 5
11
Output:
5 1 2 3 4
#include <stdio.h>
void reverse(int* arr,int s,int e){
    int i=s,j=e;
    while(i<j){
        int t=arr[i];
        arr[i]=arr[j];
        arr[j]=t;
        i++;j--;
    }
    return;
}
int* rotate(int* numbers, int length, int R){
    reverse(numbers,0,length-1);
    R=R%length;
    
    reverse(numbers,0,R-1);
    reverse(numbers,R,length-1);
    
    return numbers;
}
int main()
{
    int N,R;
    scanf("%d",&N);
    int arr[N];
    int index;
    for(index=0; index < N; index++)
    {
        scanf("%d",&arr[index]);
    }
    scanf("%d",&R);

    rotate(arr,N,R);

    for(index=0; index < N; index++)
    {
        printf("%d ",arr[index]);
    }
    return 0;
}
