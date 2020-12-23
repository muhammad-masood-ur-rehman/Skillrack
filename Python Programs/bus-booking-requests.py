Bus Booking Requests
The program must accept two integers M and N as the input, where M represents the number of buses in a row and N represents the number of days for booking seats on the buses. For each day, K seats are booked for the buses numbered from X to Y. The values of X, Y and K for each day are also passed as the input to the program. The program must print the total number of seats booked on each bus after N days as the output.
Boundary Condition(s):
2 <= M <= 100
1 <= N <= 10
1 <= X < Y <= M
1 <= K <= 50
Input Format:
The first line contains M.
The second line contains N.
The next N lines, each contains three integers representing X, Y and K separated by a space.
Output Format:
The first line contains an integer representing the total number of seats booked on each bus after N days.
Example Input/Output 1:
Input:
5
3
1 2 5
2 3 10
2 5 15
Output:
5 30 25 15 15
Explanation:
Here M = 5 and N = 3.
Initially, the number of seats booked in the five buses are 0 0 0 0 0.
On the first day, 5 seats are booked for the buses from 1 to 2.
The number of seats booked in the five buses become 5 5 0 0 0.
On the second day, 10 seats are booked for the buses from 2 to 3.
The number of seats booked in the five buses become 5 15 10 0 0.
On the third day, 15 seats are booked for the buses from 2 to 5.
The number of seats booked in the five buses become 5 30 25 15 15.
Hence the output is
5 30 25 15 15
Example Input/Output 2:
Input:
3
2
1 2 10
2 3 40
Output:
10 50 40
a,b=int(input()),int(input())
l=[0]*a
for i in range(b):
    x,y,z=map(int,input().split())
    for j in range(x-1,y):
        l[j]+=z
print(*l)
