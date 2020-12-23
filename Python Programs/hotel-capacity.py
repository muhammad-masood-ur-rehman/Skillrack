Hotel Capacity
A hotel has T tables. The number of people N1, N2, ... NT who can sit in each table is given as input. The program has to print the total capacity C of the hotel.
Input Format:
The first line contains T.
The second line contains the number of people who can sit in each table, with each value separated by a space.
Output Format:
The first line contains C.
Boundary Conditions:
1 <= T <= 100
1 <= Ni <= 10
Example Input/Output 1:
Input:
4
4 5 8 2
Output:
19
Example Input/Output 2:
Input:
10
4 6 2 6 4 8 10 6 4 4
Output:
54
n=int(input())
print(sum(int(i) for i in input().split()))
