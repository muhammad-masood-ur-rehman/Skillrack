Match Last Letter
Given two strings S1 and S2 , print the string S1 vertically with the string S2 in reversed manner which ends with the letter being considered in S1.
 
Boundary Condition :
1 <= Length of strings S1 , S2 <= 100
Input Format:
The first line contains S1
The second line contains S2
Example Input/Output 1:
Input:
INDIA
REDMI
Output :
IMDER
N
D
I
A

Example Input/Output 2:
Input:
frozen
maximum
Output :
f
r
o
z
e
n
#include<stdio.h>

#include <stdlib.h>

int main() {
    char a[100], b[100];
    scanf("%s%s", a, b);
    int l = strlen(b), i;
    for (i = 0; i < strlen(a); i++) {
        printf("%c", a[i]);
        if (a[i] == b[l - 1]) {
            for (int j = l - 2; j >= 0; j--)
                printf("%c", b[j]);
            printf("\n");
            i++;
            break;
        }
        printf("\n");
    }
    for (int j = i; j < strlen(a); j++)
        printf("%c\n", a[j]);
}
