Matrix - Inverted L & Reverse L
The program must accept an integer matrix of size NxN as the input. The program must print the layers of the matrix based on the following condition.
- For each layer of the matrix, the program must print the integers from the top-right corner to the bottom-left corner (both inclusive) in the anticlockwise direction. Then the program must print the integers from the top-right corner to the bottom-left corner (both exclusive) in the clockwise direction.
Boundary Condition(s):
2 <= N <= 50
Input Format:
The first line contains N.
The next N lines, each contains N integer values separated by a space.
Output Format:
The first N lines, each contains the integer value(s) separated by a space.
Example Input/Output 1:
Input:
4
69 50 96 12
65 66 11 94
52 76 21 37
77 38 63 49
Output:
12 96 50 69 65 52 77
94 37 49 63 38
11 66 76
21
Explanation:
Here N = 4, so the pattern contains 4 lines.
In the first layer of the matrix, the integers from the top-right to the bottom-left (both inclusive) in the anticlockwise direction are highlighted below.
69 50 96 12
65 66 11 94
52 76 21 37
77 38 63 49
So these integers are printed in the first line.
In the first layer of the matrix, the integers from the top-right to the bottom-left (both exclusive) in the clockwise direction are highlighted below.
69 50 96 12
65 66 11 94
52 76 21 37
77 38 63 49
So these integers are printed in the second line.
Similarly, the integers in the second layer of the matrix are printed in the next two lines.
Hence the output is
12 96 50 69 65 52 77
94 37 49 63 38
11 66 76
21
Example Input/Output 2:
Input:
5
36 99 61 86 95
38 55 63 58 15
64 39 84 35 43
14 89 21 34 96
68 73 28 22 37
Output:
95 86 61 99 36 38 64 14 68
15 43 96 37 22 28 73
58 63 55 39 89
35 34 21
84
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n;
scanf("%d",&n);
int arr[n][n];
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        scanf("%d",&arr[i][j]);
    }
}
for(int i=0;i<n/2+(n%2!=0);i++){
    for(int j=n-i-1;j>=i;j--){
        printf("%d ",arr[i][j]);
    }
    for(int j=i+1;j<n-i;j++){
        printf("%d ",arr[j][i]);
    }
    printf("\n");
    for(int j=i+1;j<n-i;j++){
        printf("%d ",arr[j][n-i-1]);
    }
    for(int j=n-i-2;j>i;j--){
        printf("%d ",arr[n-i-1][j]);
    }
    if(i+1!=n/2+(n%2!=0))
    printf("\n");
}

}
n=int(input())
l=[]
for x in range(n):
    l.append(list(map(int,input().split())))
C=n
R=-1
for y in range(n):
    if y%2==0:
        C-=1
        R+=1
        c=C 
        r=R
        while c>R:
            print(l[r][c],end=" ")
            c-=1
        while r<=C:
            print(l[r][c],end=" ")
            r+=1
    else:
        r=R+1
        c=C
        while r<C+1:
            print(l[r][c],end=" ")
            r+=1
        while c>R+1:
            print(l[r-1][c-1],end=" ")
            c-=1
    print()
