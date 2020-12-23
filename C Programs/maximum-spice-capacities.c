Maximum Spice Capacities
Maximum Spice Capacities: There are N bottles with different capacities filled with different types of spices. The spices are mixed in certain order to get a perfect mix. The bottle to be picked up to mix with spice is calculated by adding the capacity of the current bottle to the current position of the bottle. The chef is greedy and hence wants to mix the maximum number of different spices(not maximum capacity) to the dish. Print the capacities of the bottles to be mixed in the specified order to get maximum types of spices.
Note: If there are more than one maximum set of spices exist, print the first occurring maximum set.
Boundary Condition(s):
1 <= N <= 1000
1 <= capacity <= 100
Input Format:
The first line contains N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains integers separated by a space.
Example Input/Output 1:
Input:
5
1 2 3 4 5
Output:
1 2 4
Explanation:
Possible order of capacities are,
3 spices -> 1 2 4
2 spices -> 2 4
1 spice -> 3
1 spice -> 4
1 spice -> 5
Example Input/Output 2:
Input:
7
1 6 3 1 12 1 4
Output:
3 1 4
#include <stdio.h>

int main() {
    int n, f, m, s = 0, k;
    scanf("%d", & n);
    int a[n];
    for (int i = 0; i < n; i++)
        scanf("%d", & a[i]);
    for (int i = 0; i < n; i++) {
        k = i + 1;
        m = 1;
        while (k <= n) {
            k += a[k - 1];
            m += (k <= n);
        }
        if (m > s) {
            s = m;
            f = i + 1;
        }
    }
    while (f <= n) {
        printf("%d ", a[f - 1]);
        f += a[f - 1];
    }
}
