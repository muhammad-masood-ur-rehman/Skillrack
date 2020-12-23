Reverse X to Y Position Characters
A string S and two integers X and Y are passed as input. The program must print the characters in the string S from position X to position Y in the reverse order.
Boundary Condition(s):
1 <= Length of S <= 100
1 <= X <= Y
X <= Y <= Length of S
Input Format:
The first line contains the String S .
The second line contains X and Y separated by a space.
Output Format:
The first line contains the string value (from X to Y positions in the reverse order)
Example Input/Output 1:
Input:
skillrack
3 6
Output:
rlli
Explanation :
The characters in string S from position 3 to position 6 are illr. Hence the output is printed in the reverse order as rlli.   
Example Input/Output 2:
Input:
meteorology
4 7
Output:
oroe
Explanation :
The characters in string S from position 4 to position 7 are eoro. Hence the output is printed in the reverse order as oroe. 
s=input().strip()
a,b=map(int,input().split())
s=s[a-1:b]
print(s[::-1])
