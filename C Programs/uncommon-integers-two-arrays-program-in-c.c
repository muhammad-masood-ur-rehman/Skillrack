Uncommon Integers - Two Arrays Program in C
The program must accept two integer arrays of sizes M and N as the input. The program must print all the uncommon integer(s) (ascending order) in the given two arrays. If there is no uncommon integer in the given two arrays then the program must print -1 as the output.
Boundary Condition(s):
1 <= M, N <= 10000
Input Format:
The first line contains the values of M and N separated by a space.
The second line contains M integers separated by space(s).
The third line contains N integers separated by space(s).
Output Format:
The first line contains either all the uncommon integer(s) separated by space(s) or -1.
Example Input/Output 1:
Inp ut:
5 5
87 5 6 12 91
5 1 7 87 8
Output:
1 6 7 8 12 91
Explanation:
The uncommon integers in the first array are 6 12 91
The uncommon integers in the second array are 1 7 8
The uncommon integers from both the arrays are combined and sorted in ascending order.
Hence the output is 1 6 7 8 12 91
Example Input/Output 2:
Input:
10 6
37 79 94 50 92 7 6 23 98 6
6 7 57 85 55 78
Output:
23 37 50 55 57 78 79 85 92 94 98
Explanation:
The uncommon integers in the first array are 37 79 94 50 92 23 98
The uncommon integers in the second array are 57 85 55 78
The uncommon integers from both the arrays are combined and sorted in ascending order.
Hence the output is 23 37 50 55 57 78 79 85 92 94 98
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int num1,num2,counter=0;
    int array1[1000001]={0},array2[1000001]={0};
    
    scanf("%d%d",&num1,&num2);
    
    int arr1[num1];
    int arr2[num2];
    
    for(int ele=0;ele<num1;ele++){
        scanf("%d",&arr1[ele]);
        array1[arr1[ele]]=1;
    }
    for(int ele=0;ele<num2;ele++){
        scanf("%d",&arr2[ele]);
        array2[arr2[ele]]=1;
    }
    for(int ele=1;ele<1000001;ele++){
        if((array1[ele] || array2[ele]) && array1[ele]!=array2[ele]){
            printf("%d ",ele);
            counter=1;
        }
    }
    if(!counter)printf("-1");    
    return 0;
}
