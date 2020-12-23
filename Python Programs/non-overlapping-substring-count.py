Non-overlapping Substring Count
Two string values S and P representing a string and pattern are passed as the input to the program. The program must print the number of non-overlapping occurrences of pattern P in the string S as the output.
Note: The string S and pattern P contains only lowercase alphabets.
Boundary Condition(s):
1 <= Length of S <= 10^5
1 <= Length of P <= 10
Input Format:
The first line contains S.
The second line contains P.
Output Format:
The first line contains the number of non-overlapping occurrences of P in S.
Example Input/Output 1:
Input:
abababa
aba
Output:
2
Explanation:
The pattern aba occurs two times on abababa without overlapping. So 2 is printed.
Example Input/Output 2:
Input:
techchampcheckin
ch
Output:
3
s1=input().strip()
s2=input().strip()
c=s1.count(s2)
print(c)
