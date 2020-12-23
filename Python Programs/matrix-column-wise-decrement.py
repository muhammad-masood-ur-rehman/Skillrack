Matrix - Column-wise Decrement
Matrix - Column-wise Decrement: Given an integer N then form an N*N matrix by assigning the value N as starting value and incrementing each successive cell value by N for the first row and from the second row decrement the values column-wise by the column number. Then the program must print the matrix.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains N.
Output Format:
Matrix Pattern.
Example Input/Output 1:
Input:
3
Output:
3 6 9
2 4 6
1 2 3
Example Input/Output 2:
Input:
4
Output:
4 8 12 16
3 6 9 12
2 4 6 8
1 2 3 4
Python:
a=int(input())
for i in range(a,0,-1):
   for j in range(1,a+1):
       print(i*j,end=' ')
   print()
n=int(input())
for i in range(n,0,-1):
    k=i 
    for j in range(n,0,-1):
        print(k,end=" ")
        k+=i 
    print()
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int store=n;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%d ",(j+1)*store);
        }
        store--;
        printf("\n");
    }

}
