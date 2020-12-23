Python Program To Check Triplet Sum
N integers are passed as input to the program. The program must print the count of triplets (combination of three integers) which add up to a given sum S.
Boundary Condition(s):
1 <= N <= 25
-10^5 <= S <= 10^5
Input Format:
The first line contains N.
The second line contains N integer values separated by a space.
The third line contains S.
Output Format:
The first line contains the count of triplets whose sum is S.
Example Input/Output 1:
Input:
4
10 20 50 20
50
Output:
1
Explanation:
Here the required sum S=50.
The only triplet whose sum is 50 is
10 20 20
Example Input/Output 2:
Input:
7
3 9 -10 7 -12 -2 -5
0
Output:
3
Explanation:
Here the required sum S=0.
The three triplets whose sum is 0 are
3 9 -12
7 -2 -5
3 7 -10
from itertools import combinations as c 
n=int(input())
l=list(map(int,input().split()))
d=int(input())
p=0
for i in list(c(l,3)):
    if sum(i)==d:
        p+=1 
print(p)
