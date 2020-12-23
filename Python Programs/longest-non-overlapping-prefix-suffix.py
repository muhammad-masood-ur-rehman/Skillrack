Longest Non-Overlapping Prefix Suffix
Longest Non-Overlapping Prefix Suffix: The program must accept a string S as the input. Then the program must print the the longest prefix in the string S which is also a suffix. The prefix and the suffix must not overlap. If there is no such prefix, then the program must print -1 as the output.
Boundary Condition(s):
1 <= Length of S <= 10^8
Note: Optimize your algorithm to avoid Timeout.
Input Format:
The first line contains the value of S.
Output Format:
The first line contains the string representing the longest prefix which is also a suffix.
Example Input/Output 1:
Input:
abcefgabc
Output:
abc
Explanation:
Here abc is the longest prefix which is also present as a suffix.
Example Input/Output 2:
Input:
skillrack
Output:
-1
Example Input/Output 3:
Input:
tutortutor
Output:
tutor
def LengthlongestPrefixSuffix(s): 
	n = len(s) 
	lps = [0 for i in range(n)] 
	len1 = 0
	i = 1
	while (i < n): 
		if (s[i] == s[len1]): 
			len1 += 1
			lps[i] = len1 
			i += 1
		
		else:
			if (len1 != 0): 
				len1 = lps[len1 - 1] 
			else: 
				lps[i] = 0
				i += 1
	res = lps[n - 1]
	
	if (res > int(n / 2)): 
		return int(n / 2) 
	else: 
		return res 
def longestPrefixSuffix(s): 
	len1 = LengthlongestPrefixSuffix(s) 
	prefix = "" 
	for i in range(len1): 
		prefix += s[i] 
	return prefix 

s =input().strip()
ans = longestPrefixSuffix(s) 
if (ans == ""): 
	print("-1") 
else: 
	print(ans)
