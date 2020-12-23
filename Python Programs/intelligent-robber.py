Intelligent Robber
There are N streets in a town and in each street there is one treasure house with certain number of gold coins - C(1) .... C(N) in it. As the robber is intelligent, in order not to get caught, if he robs in a house in a given street he does not rob in the houses in the two streets which are adjacent to the house robbed (either to it's left or right). Thus he avoids awareness among the people and his risk is reduced.
Given N and the coins C(i) (where i= 1 to N) in each of the treasure house, find the maximum gold coins M, that the robber can acquire.
Input Format:
The first line contains N.
The second line contains N positive integers representing the gold coins in each of the N treasure houses.
Output Format:
The first line contains M which represents the maximum number of gold coins the robber can acquire.
Boundary Conditions:
3 <= N <= 999999
1 <= C(i) <= 100
Example Input/Output 1:
Input:
4
5 3 11 20
Output:
25
Example Input/Output 2:
Input:
7
10 20 15 1 9 12 5
Output:
32
n,a=int(input()),[int(i) for i in input().split()]
x,y,z=a[0],max(a[0],a[1]),max(a[0],a[1],a[2])
for i in range(3,n):
    t=max(x+a[i],y,z)
    x,y=y,t
print(t)
