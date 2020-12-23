Longest Substring with a and b count
Longest Substring with a and b count: A string S containing only the characters a and b is passed as the input. The program must print the length L of the longest substring with equal numbers of a and b in it.
Note: Optimize the algorithm so that the program executes successfully within the time limit.
Boundary Condition(s):
1 <= Length of string S<= 100000
Input Format:
The first line contains the string S.
Output Format:
The first line contains the L.
Example Input/Output 1:
Input:
abaabba
Output:
6
Example Input/Output 2:
Input:
aaabaaabbbaaab
Output:
8
def stringLen(str): 
	m = dict() 
	m[0] = -1
	ca = 0
	cb = 0
	res = 0
	for ele in range(len(str)): 
		if str[ele] == 'a': 
			ca += 1
		else: 
			cb += 1
		if m.get(cb - ca): 
			res = max(res, ele - m[cb - ca]) 
		else: 
			m[cb - ca] = ele 
	return res 

stri = input()
print(stringLen(stri))
