Parking Charges
Parking Charges Program: In a parking space, N vehicles are parked. The parking charge for each vehicle is calculated based on how long it has been parked. The parking charge per hour may vary depending on the type of vehicle. The parking charge of a vehicle is calculated based on the following conditions.
- If a vehicle is parked for H hours and M minutes and the parking charge for the vehicle is P rupees per hour, then the total parking charge is H * P if M is less than or equal to 30. Else the total parking charge is (H + 1) * P.
- If a vehicle is parked for less than or equal to 30 minutes, then the total parking charge is P.
The parking time (Hours:Minutes) and the parking charge per hour for each vehicle are passed as the input to the program. The program must print the number of vehicles parked for more than X hours and Y minutes. Then the program must print the number of vehicles charged above Z rupees as the output.
Boundary Condition(s):
2 <= N <= 100
0 <= H, X <= 23
0 <= M, Y <= 59
1 <= P, Z <= 1000
Input Format:
The first line contains N.
The N lines, each contains the parking time and the parking charge per hour separated by a space.
The (N+2)nd line contains X, Y and Z separated by a space.
Output Format:
The first line contains an integer representing the number of vehicles parked for more than X hours and Y minutes.
The second line contains an integer representing the number of vehicles charged above Z rupees.
Example Input/Output 1:
Input:
4
02:45 10
03:20 25
02:55 15
05:30 35
3 15 50
Output:
2
2
Explanation:
Here X = 3, Y = 15 and Z = 50.
For the 1st vehicle, the parking time is 02:45 and the total parking charge is 30 ((2 + 1) * 10).
For the 2nd vehicle, the parking time is 03:20 and the total parking charge is 75 (3 * 25).
For the 3rd vehicle, the parking time is 02:55 and the total parking charge is 45 ((2 + 1) * 15).
For the 4th vehicle, the parking time is 05:30 and the total parking charge is 175 (5 * 35).
The number of vehicles parked for more than 3 hours and 15 minutes is 2.
The number of vehicles charged above 50 rupees is 2.
Hence the output is
2
2
Example Input/Output 2:
Input:
6
00:30 15
04:45 20
01:00 10
05:30 20
02:31 12
00:45 30
0 59 30
Output:
4
3
n=int(input())
l=[input().strip() for i in range(n)]
x,y,z=map(int,input().split())
p_count,t_count=0,0
t_time=x*60+y 
for i in range(n):
    a,b=l[i].split()[0].split(':')
    c=l[i].split()[1]
    p=0
    time=int(a)*60+int(b)
    if time<=30:
        p=int(c)
    elif int(b)<=30:
        p=int(a)*int(c)
    else:
        p=int(c)*(int(a)+1)
    if p>z:
        p_count+=1
    if int(a)*60+int(b)>t_time:
        t_count+=1
print(t_count)
print(p_count)
