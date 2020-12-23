Convert 12 hour time to 24 hour format
The time in 12 hour format is passed as an input. The program must print it in 24 hour format.
Input Format:
The first line contains the value of time in 12 hour format.
Output Format:
The first line contains the value of the string in 24 hour format.
Example Input/Output 1:
Input:
12:43:52PM
Output:
12:43:52
Example Input/Output 2:
Input:
12:10:12AM
Output:
00:10:12
Example Input/Output 3:
Input:
04:22:42PM
Output:
16:22:42
Example Input/Output 4:
Input:
11:22:18AM
Output:
11:22:18
str1=input().strip()
if str1[-2:] == "AM" and str1[:2] == "12":
   print("00" + str1[2:-2])
elif str1[-2:] == "AM":
   print(str1[:-2])
elif str1[-2:] == "PM" and str1[:2] == "12":
   print(str1[:-2])
else:
   print(str(int(str1[:2]) + 12) + str1[2:8]) 
