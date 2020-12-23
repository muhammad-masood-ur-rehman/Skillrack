Two Digital Clocks
Two digital clocks C1 and C2 (in 24-hr format) are hanging in a room showing two different times in chronological order. The program must accept the current time on the clocks C1, C2 and another time T as the input. The program must print the time on the clock C2 when the time on the clock C1 is T.
Input Format:
The first line contains C1.
The second line contains C2.
The third line contains T.
Output Format:
The first line contains the time on the clock C2 when the time on the clock C1 is T.
Example Input/Output 1:
Input:
10:30
12:00
12:45
Output:
14:15
Explanation:
Here C1 = 10:30, C2 = 12:00 and T = 12:45.
The difference between 10:30 and 12:00 is 1 Hour and 30 Minutes.
If C1 shows 12:45, then C2 shows 14:15.
So 14:15 is printed as the output.
Example Input/Output 2:
Input:
05:20
22:23
09:30
Output:
02:33
a,b=map(int,input().split(":"))
c,d=map(int,input().split(":"))
e,f=map(int,input().split(":"))
difference=(c*60+d)-(a*60+b)
result=(e*60+f)+difference
print("%02d:%02d"%(result//60%24,result%60))
