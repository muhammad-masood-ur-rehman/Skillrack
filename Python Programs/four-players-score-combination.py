Four Players Score Combination
Four Players Score Combination: The program must accept the score of N players in a cricket match. The program must print the number of combinations with exactly 4 players and total runs scored by the 4 players is greater than or equal to 100 as the output.
Boundary Condition(s):
4 <= N <= 250
Input Format:
The first line contains N.
The second line contains N integers separated by space.
Output Format:
The first line contains the number of combinations as mentioned above.
Example Input/Output 1:
Input:
6
20 50 20 10 30 25
Output:
10
Example input/output 2:
Input:
8
32 11 40 60 26 23 66 43
Output:
69
from itertools import combinations as c
n=int(input())
l=list(map(int,input().split()));k=0
for i in list(c(l,4)):
    if sum(i)>=100:k+=1
print(k)
