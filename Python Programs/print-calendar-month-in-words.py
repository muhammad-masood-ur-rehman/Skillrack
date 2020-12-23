Print Calendar Month in Words
The program must accept an integer value N and print the corresponding calendar month in words. 1 - January, 2 - February, …. , 11 - November, 12 - December If any value apart from 1 to 12 is passed as input, the program must print "Invalid Input".
Input Format: The first line denotes the value of N.
Output Format: The first line contains the output as per the description. (The output is CASE SENSITIVE).
Boundary Conditions: 1 <= N <= 12
Example Input/Output 1:
Input:
5
Output:
May
Example Input/Output 2:
Input:
12
Output:
December
Example Input/Output 3:
Input:
105
Output:
Invalid Input
import datetime
n=int(input())
if(n<=12):
    print(datetime.date(1900,n,1).strftime('%B'))      //python won’t handle before 1900
else:
    print("Invalid Input")
