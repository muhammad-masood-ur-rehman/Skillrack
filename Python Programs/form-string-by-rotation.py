Form String by Rotation
Given two strings S1 and S2, print yes if S2 can be obtained by rotating the string S1. Else print no.
Boundary Condition(s):
1 <= Length of S1, S2 <= 10000
Input Format:
The first line contains S1 and S2 separated by space.
Output Format:
The first line contains Yes if S2 can be obtained by rotating S1 else No.
Example Input/Output 1:
Input:
hello llohe
Output:
Yes
Example Input/Output 2:
Input:
Question tionseuQ
Output:
No
def areRotations(string1, string2): 
	size1 = len(string1) 
	size2 = len(string2) 
	temp = '' 
	if size1 != size2: 
		return 0
	temp = string1 + string1 
	if (temp.count(string2)> 0): 
		return 1
	else: 
		return 0
string1,string2=map(str,input().split())

if areRotations(string1, string2): 
	print("Yes")
else: 
	print("No")
