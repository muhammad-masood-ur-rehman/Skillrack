Palindromic Partition
The program must accept a string S as the input. The program must print the minimum number of cuts required so that all the substring values in S are palindromes as the output.
Boundary Condition(s):
1 <= Length of S <= 1000
Input Format:
The first line contains the string S.
Output Format:
The first line contains the minimum number of cuts required so that all the substring values in S are palindromes.
Example Input/Output 1:
Input:
evening
Output:
2
Explanation:
Here the minimum number of cuts required is 2.
After two cuts in the string "evening", the palindromic substring values are "eve", "nin" and "g".
Example Input/Output 2:
Input:
rotator
Output:
0
Example Input/Output 3:
Input:
waitingnight
Output:
7
import sys 
def minPalPartion(str1): 
	n = len(str1); 
	C = [0]*(n+1); 
	P = [[False for x in range(n+1)] for y in range(n+1)]; 
	for i in range(n): 
		P[i][i] = True; 
	for L in range(2, n + 1): 
		for i in range(n - L + 1): 
			j = i + L - 1;
			if (L == 2): 
				P[i][j] = (str1[i] == str1[j]); 
			else: 
				P[i][j] = ((str1[i] == str1[j]) and P[i + 1][j - 1]); 
	for i in range(n): 
		if (P[0][i] == True): 
			C[i] = 0; 
		else: 
			C[i] = sys.maxsize; 
			for j in range(i): 
				if(P[j + 1][i] == True and 1 + C[j] < C[i]): 
					C[i] = 1 + C[j]; 
	return C[n - 1]; 
str1 = input().strip(); 
print(minPalPartion(str1));
