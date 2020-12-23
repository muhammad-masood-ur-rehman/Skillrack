Sort N Strings - Descending Order
N strings are passed as input. The program must sort them in the descending order. 
Input Format: The first line contains the value of N. Next N lines contain the value of N string values. 
Output Format: N lines containing the N string values sorted in descending order. 
Boundary Conditions: 2 <= N <= 15 Length of a string is between 2 and 100. 
Example Input/Output 1: 
Input: 6 
Apple 
banana 
Boy 
Zoo 
Hat 
heckle 
Output: 
heckle 
banana 
Zoo 
Hat 
Boy 
Apple
n=int(input())
st=[input().strip() for ele in range(n)]
st.sort(reverse=True)
print(*st,sep="\n")
