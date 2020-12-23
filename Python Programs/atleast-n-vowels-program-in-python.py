Atleast N Vowels Program in Python
Atleast N Vowels: A string S is passed as the input to the program along with a positive integer value N. The program must print Yes if the string S contains atleast N vowels. Else it must print No.
Boundary Condition(s):
1 <= Length of String S <= 1000
1 <= N <= 1000
Input Format:
The first line contains the value of S
The second line contains the value of N
Output Format:
The first line contains Yes or No
Example Input/Output 1:
Input:
machine
2
Output:
Yes
Example Input/Output 2:
Input:
college
4
Output:
No
s=input().strip().lower()
n=int(input());c=0
for i in s:
    if i in 'aeiou':c+=1
print('Yes')if c>=n else print('No')
