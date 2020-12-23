Inverted L-Shaped Matrix
Given a squarematrix of size S, print the matrix in the format given in Example Input/Output section.
Input Format:
The first line contains the value size S of the matrix.
The next S lines contain S values of a given row separated by a space.
Output Format:
The S lines denote the inverted L-shaped matrix.
Boundary Condition:
1 <= S <= 100
Example Input/Output 1:
Input:
3
11 12 13
21 22 23
31 32 33
Output:
11
21 22 12
31 32 33 23 13
Example Input/Output 2:
Input:
6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
Output:
1
1 2 2
1 2 3 3 3
1 2 3 4 4 4 4
1 2 3 4 5 5 5 5 5
1 2 3 4 5 6 6 6 6 6 6
#include<stdio.h>

#include <stdlib.h>

int main() {
    int i, n, j, k, p, q, a[100][100];
    scanf("%d", & n);
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d ", & a[i][j]);
        }
    }
    p = 1;
    for (i = 0; i < n; i++) {
        for (q = 0; q < p; q++) {
            printf("%d ", a[i][q]);
        }
        for (q = i - 1; q >= 0; q--) {
            printf("%d ", a[q][i]);
        }
        printf("\n");
        p++;
    }

}
