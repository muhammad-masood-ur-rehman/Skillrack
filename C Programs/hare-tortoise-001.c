Hare & Tortoise - 001
Most of us would know the Hare & the Tortoise story. As the hare can run faster than the tortoise, god gives some magical power points X to the tortoise which never diminishes. But to be fair, god also gives an array of L magical power points to the Hare before each lap involved in the race. When the hare acquires N or more magical power points due to laxity it goes to sleep and during sleep it loses exactly N magical power points. Then the hare wakes up and completes the remaining laps. If in the last lap the magical power points R remaining with the hare is more than X, Hare wins. Else tortoise wins. If R is equal to X, the match ends in a draw and the program must print -1. If the hare does not sleep, it will always win the race. The hare will sleep only once or not sleep at all.
Input Format:
First line contains N and X power points separated by a space
Second line contains L which denotes the number of laps in the race.
Third line contains L power points values separated by a space
Output Format:
First line contains HARE or TORTOISE or -1 based on the match result.
Example Input/Output 1:
Input:
5 9
5
1 2 3 4 5
output:
HARE
Example Input/Output 2:
Input:
5 11
5
1 2 3 4 5
output:
TORTOISE
#include<stdio.h>

#include <stdlib.h>

int main() {
    long int n, x, l, i, c = 0, r = 0;
    scanf("%li%li%li", & n, & x, & l);
    long int a[l];
    for (i = 0; i < l; i++)
        scanf("%li", & a[i]);
    for (i = 0; i < l; i++)
        r = r + a[i];
    if (r >= n) {
        r = r - n;
        c++;
    }
    if (r > x || c == 0)
        printf("HARE");
    else if (r < x)
        printf("TORTOISE");
    else
        printf("-1");
}
