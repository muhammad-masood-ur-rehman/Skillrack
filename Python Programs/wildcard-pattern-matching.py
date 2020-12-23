Wildcard Pattern Matching
The program must accept a text and a wildcard pattern as the input. The program must print "Matching" if the wildcard is matched with text. Else the program must print "Not matching" as the output.
The wildcard pattern can include the characters '?' and '*'
'?' – Matches any single character
'*' – Matches any sequence of characters (including the empty sequence)
Boundary Condition(s):
1 <= Length of text <= 100
1 <= Length of wildcard pattern <= 50
Input Format:
The first line contains the text.
The second line contains the wildcard pattern.
Output Format:
The first line contains either "Matching" or "Not matching".
Example Input/Output 1:
Input:
abbbbbbbbccbbbbbed
a*b?d
Output:
Matching
Explanation:
The wildcard pattern is "a*b?d".
'*' can be replaced by "bbbbbbbbccbbbb".
'?' can be replaced by "e".
Hence the output is Matching
Example Input/Output 2:
Input:
abbbbbbbbccbhd
a*b??b?d
Output:
Matching
Example Input/Output 3:
Input:
abbbbbbbbccbhd
*c??b?d
Output:
Not matching
def strrmatch(strr, pattern, n, m): 
	if (m == 0): 
		return (n == 0) 
	lookup = [[False for i in range(m + 1)] for j in range(n + 1)] 
	lookup[0][0] = True
	for j in range(1, m + 1): 
		if (pattern[j - 1] == '*'): 
			lookup[0][j] = lookup[0][j - 1] 
	for i in range(1, n + 1): 
		for j in range(1, m + 1): 
			if (pattern[j - 1] == '*'): 
				lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j] 
			elif (pattern[j - 1] == '?' or strr[i - 1] == pattern[j - 1]): 
				lookup[i][j] = lookup[i - 1][j - 1] 
			else: 
				lookup[i][j] = False
	return lookup[n][m] 
strr = input().strip()
pattern = input().strip()
if (strrmatch(strr, pattern, len(strr),len(pattern))): 
	print("Matching") 
else: 
	print("Not matching")
