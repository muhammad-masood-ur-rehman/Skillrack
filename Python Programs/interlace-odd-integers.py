Interlace Odd Integers
The Program must accept M and N integers as the input. The Program must interlace and print the odd integers among the M integers in forward order and the odd integers among the N integers in reverse order.
Boundary Condition(s):
1 <= M, N <= 1000
1 <= Each integer value <= 10^5
Input Format:
The first line contains the integers M and N seperated by space(s).
The second line contains M integers seperated by space(s).
The third line contains N integers seperated by space(s).
Output Format:
The first line contains odd integers as per the given conditions seperated by a space.
Example Input/Output 1:
Input:
5 6
23 54 65 21 65
76 97 32 16 87 54
Output:
23 87 65 97 21 65
Explanation:
M = 5 and N = 6
The odd integers among the M integers in forward order are 23 65 65.
The odd integers among the N integers in reverse order are 87 97.
By Interlacing these odd integers we get 23 87 65 97 21 65.
Example Input/Output 2:
Input:
7 8
4 5 1 2 8 9 3
0 5 3 8 1 6 7 9
Output:
5 9 1 7 9 1 3 3 5
Python:
def odd(l):
    l=[i for i in l if i%2==1]
    return l

x,y=map(int,input().split())

a=list(map(int,input().split()))
m=odd(a)

b=list(map(int,input().split()))
n=odd(b)[::-1]

for i in range(max(len(m),len(n))):
    if i<len(m):
        print(m[i],end=' ')
    if i<len(n):
        print(n[i],end=' ')
C:
#include<stdio.h>
#include <stdlib.h>
int input(int n,int* arr){
    for(int ele=0;ele<n;ele++)scanf("%d",&arr[ele]);
}
int main()
{
    int num1,num2;
    scanf("%d%d",&num1,&num2);
    
    int arr1[num1],arr2[num2];
    input(num1,arr1);
    input(num2,arr2);
    
    int s1=0,s2=num2-1,ctr=1;
    while(s1<num1 && s2>=0){
        if(ctr==1){
            if(arr1[s1]%2){
                printf("%d ",arr1[s1]);
                ctr=2;
            }
            s1++;
        }
        else{
            if(arr2[s2]%2==1){
                printf("%d ",arr2[s2]);
                ctr=1;
            }
            s2--;
        }
    }
    while(s1<num1){
        if(arr1[s1]%2==1)printf("%d ",arr1[s1]);
        s1++;
    }
    while(s2>=0){
        if(arr2[s2]%2==1)printf("%d ",arr2[s2]);
        s2--;
    }
    return;
}
