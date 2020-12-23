Largest Integer
The casino has introduced a new game in which there are M vertical chutes each containing N single digit (possibly zero) numbers. You can choose any chute and draw the bottom number and when you do this all the other numbers in the chute descend by one slot. You need to build the largest integer using this process drawing all the numbers from the chutes. For example, in the following example, we have three chutes of four numbers each and the largest number that can be drawn is 469534692781. Given the number of chutes and the numbers in each chute, write a program to find the largest integer that could be formed using the above process.
Boundary Condition(s):
1 <= M <= 20
1 <= N <= 50
Input Format:
The first line contains M, N two comma separated integers giving the number of chutes and the number of digits in each chute.
The next M lines each contain N comma separated digits, giving the digits from top to bottom in each of the chutes.
Output Format: 
One line containing the largest integer that could be formed.
Example Input/Output1:
Input:
4,4
7,5,5,2
3,6,1,7
8,7,0,4
8,7,3,9
Output:
9743782557163078

Explanation:
The chutes are represented as below,

Example Input/Output2:
Input:
2,3
1,2,3
2,4,6
Output:
643221

#include<stdio.h>

#include <stdlib.h>

int main() {
    int r, c;
    scanf("%d,%d", & r, & c);
    char a[r][c];
    int n[r];
    for (int i = 0; i < r; i++) {
        n[i] = c - 1;
        for (int j = 0; j < c; j++)
            scanf(" %c, ", & a[i][j]);
    }
    for (int i = 0; i < r * c; i++) {
        int p = -1;
        for (int j = 0; j < r; j++) {
            if (p == -1 && n[j] >= 0)
                p = j;
            else if (p != -1 && n[j] >= 0 && a[j][n[j]] > a[p][n[p]])
                p = j;
            else if (p != -1 && n[j] >= 0 && a[j][n[j]] == a[p][n[p]]) {
                int f = 0;
                while (n[j] - f >= 0 && n[p] - f >= 0 && a[j][n[j] - f] == a[p][n[p] - f])
                    f++;
                if (n[j] - f >= 0 && n[p] - f >= 0 && a[j][n[j] - f] > a[p][n[p] - f])
                    p = j;
                else if (n[p] - f == -1 && n[j] - f >= 0)
                    p = j;
            }
        }
        printf("%c", a[p][n[p]--]);
    }
}
