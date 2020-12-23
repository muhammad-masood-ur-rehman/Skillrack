LRU Cache - Miss Count
The least recently used (LRU) cache algorithm evicts the element from the cache that was least recently used when the cache is full. After an element is requested from the cache, it should be added to the cache (if not there) and considered the most recently used element in the cache whether it is newly added or was already existing. Initially, the cache is empty. Implement the function lruCountMiss so that the function returns an integer indicating the number of cache misses M using the LRU cache algorithm execution for the given input. Assume that the array pages always have pages numbered from 0 to 50. (A hit means the requested page is already existing in the cache and a miss means the requested page is not found in the cache).
Input Format: The first line contains the cache size S and the number of page requests N separated by a space. The second line containing the N pages being requested from the cache.
Output Format: The first line contains the miss count M.
Boundary Conditions:
2 <= S <= N
2 <= N <= 100
Example Input/Output 1:
Input:
3 16
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0
Output:
11
Example Input/Output 2:
Input:
2 9
2 3 1 3 2 1 4 3 2
Output:
8
#include <stdio.h>

int main() {
    int i, j, k, a, b, c, d, e, f, n, n1, miss = 1;
    scanf("%d %d", & n, & n1);
    int l[10000], l1[10000];
    for (i = 0; i < n; i++)
        scanf("%d ", & l[i]);
    a = 0;
    int start = 0;
    for (i = 0; i < n; i++) {
        b = 0;
        if (a == 0)
            l1[a++] = l[i];
        else {
            for (j = start; j < a; j++) {
                if (l[i] == l1[j]) {
                    for (k = j; k < a; k++)
                        l1[k] = l1[k + 1];
                    l1[a - 1] = l[i];
                    b = 1;
                    break;
                }
            }
            if (b == 0) {
                miss += 1;
                if (a - start == n1) {
                    start++;
                    l1[a] = l[i];
                    a++;
                } else {

                    l1[a] = l[i];
                    a++;
                }

            }
        }
        for (j = start; j < a; j++)
            printf("%d ", l1[j]);
        printf("\n");

    }
    printf("%d ", miss);
}
s,n=map(int,input().strip().split(" "))
p=list(map(int,input().strip().split(" ")))
c,m=[],0
for i in p:
    if i in c:
        c.remove(i)
    else:
        if len(c)>=s:
            c.pop(0)
        m+=1
    c.append(i)
print(m)
