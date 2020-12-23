Find AM or PM
A string S which represents the time in 24 hour format HH:MM is passed as input. The program must find if it is AM or PM and print it as output. If an invalid time is passed as input, the program must print INVALIDINPUT
Boundary Conditions: 12:00 is noon and PM must be printed as output. 00:00 or 24:00 is midnight and AM must be printed as output.
Input Format: First line will contain the string value S which represents the time in HH:MM format.
Output Format: The first line will contain the output which is either AM or PM IMPORTANT: The output is case sensitive. Hence print AM or PM in upper case.
Sample Input/Output:
Example 1: Input:
13:44
Output:
PM
Example 2: Input:
12:00
Output:
PM
Example 3: Input:
32:70
Output:
INVALIDINPUT
Example 4: Input:
05:32
Output:
AM
Code:
from datetime import datetime
n=input()
h,m=n.split(":")
if int(h)>=0 and int(h)<23:
    d=datetime.strptime(n,"%H:%M")
    print(d.strftime("%p"))

else:
    print("INVALIDINPUT")
