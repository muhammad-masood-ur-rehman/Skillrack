Vehicle Pooling - Fully Occupied Program In Python
A group of N people are on a tour and they pool R vehicles to travel. The capacity of the R vehicles are passed as the input. In how many ways W can these N people accommodated in the vehicles in such a way that all the vehicles are occupied to their capacity.
Boundary Condition(s):
1 <= R <= 25
2 <= N <= 500
Input Format:
The first line contains N and R separated by a space.
The second line contains R integer values separated by a space.
Output Format:
The first line contains the value of W.
Example Input/Output 1:
Input:
15 4
10 20 5 15
Output:
2
Explanation:
15 people can occupy in two ways so that all vehicles are full.
Way-1: Vehicles with capacity 10 and 5
Way-2: Vehicle with capacity 15
Example Input/Output 2:
Input:
100 8
20 20 10 15 5 40 50 25
Output:
12
from itertools import combinations as c 
a,b=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(1,a+1):
    for j in list(c(l,i)):
        if sum(j)==a:
            p+=1
print(p)
