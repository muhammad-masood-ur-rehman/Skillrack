Chakravyuha - TCS CodeVita
Chakravyuha - TCS CodeVita: During the battle of Mahabharat, when Arjuna was far away in the battlefield, Guru Drona made a Chakravyuha formation of the Kaurava army to capture Yudhisthir Maharaj. Abhimanyu, young son of Arjuna was the only one amongst the remaining Pandava army who knew how to crack the Chakravyuha. He took it upon himself to take the battle to the enemies.
Abhimanyu knew how to get power points when cracking the Chakravyuha. So great was his prowess that rest of the Pandava army could not keep pace with his advances. Worried at the rest of the army falling behind, Yudhisthir Maharaj needs your help to track of Abhimanyu's advances. Write a program that tracks how many power points Abhimanyu has collected and also uncover his trail.
A Chakravyuha is a wheel-like formation as given below.

A Chakravyuha has a very well-defined coordinate system. Each point on the coordinate system is manned by a certain unit of the army. The Commander-In-Chief is always located at the center of the army to better coordinate his forces. The only way to crack the Chakravyuha is to defeat the units in sequential fashion.
A Sequential order of units differs structurally based on the radius of the Chakra. The radius can be thought of as length or breadth of the matrix. The structure i.e. placement of units in sequential order.
The entry point of the Chakravyuha is always at the (0,0) coordinate of the matrix. This is where the 1st army unit guards. From (0,0) i.e. 1st unit Abhimanyu has to march towards the center at (2,2) where the 25th i.e. the last of the enemy army unit guards. Remember that he has to proceed by destroying the units in sequential fashion. After destroying the first unit, Abhimanyu gets a power point. Thereafter, he gets one after destroying army units which are multiples of 11. You should also be an in a position to tell Yudhisthir Maharaj the location at which Abhimanyu collected his power points. 
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains N.
Output Format: 
The First N lines contain the N*N matrix.
The (N+1)th line contains the total power points collected.
The subsequent lines contain the coordinates of power points collected in sequential order (one per line).
Example Input/Output1:
Input:
3
Output:
1 2 3
8 9 4
7 6 5
Total Power points : 1
(0,0)
Example Input/Output2:
Input:
8
Output:
1 2 3 4 5 6 7 8
28 29 30 31 32 33 34 9
27 48 49 50 51 52 35 10
26 47 60 61 62 53 36 11
25 46 59 64 63 54 37 12
24 45 58 57 56 55 38 13
23 44 43 42 41 40 39 14
22 21 20 19 18 17 16 15
Total Power points : 6
(0,0)
(3,7)
(7,0)
(1,5)
(6,1)
(5,5)
#include<stdio.h>

#include <stdlib.h>

int main() {
  int n, s = 0, f = 1;
  scanf("%d", & n);
  int a[n][n], r = 0, c = 0, l = n, k = n, p[1000][2];
  while (r < l && c < k) {
    for (int i = c; i < k; i++) {
      a[r][i] = ++s;
      if (s % 11 == 0) {
        p[f][0] = r;
        p[f++][1] = i;
      }
    }
    r++;
    for (int i = r; i < l; i++) {
      a[i][k - 1] = ++s;
      if (s % 11 == 0) {
        p[f][0] = i;
        p[f++][1] = k - 1;
      }
    }
    k--;
    if (r < l) {
      for (int i = k - 1; i >= c; i--) {
        a[l - 1][i] = ++s;
        if (s % 11 == 0) {
          p[f][0] = l - 1;
          p[f++][1] = i;
        }
      }
      l--;
    }
    if (c < k) {
      for (int i = l - 1; i >= r; i--) {
        a[i][c] = ++s;
        if (s % 11 == 0) {
          p[f][0] = i;
          p[f++][1] = c;
        }
      }
      c++;
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++)
      printf("%d ", a[i][j]);
    printf("\n");
  }
  printf("Total Power points : %d\n", f);
  printf("(0,0)\n");
  for (int i = 1; i < f; i++)
    printf("(%d,%d)\n", p[i][0], p[i][1]);
}
