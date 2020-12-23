String Compression
String Compression: Given a string S, compress the string by its character and its count as specified in the sample input output.
Example1:
input:
aaabbbbcc
output:
a3b4c2
Example2:
input:
abc
output:
a1b1c1
#include<stdio.h>
#include <stdlib.h>

int main() {
    char arr[10000];
    int a, count = 1;
    scanf("%s", arr);
    a = strlen(arr);
    for (int i = 0; i < a; i++) {
        if (arr[i] == arr[i + 1]) {
            count++;
        }
        else {
            printf("%c%d", arr[i], count);
            count = 1;
        }
    }
}
