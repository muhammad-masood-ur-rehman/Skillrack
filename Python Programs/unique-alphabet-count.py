Unique Alphabet Count
A string S is passed as input to the program which has only alphabets (all alphabets in lower case). The program must print the unique count of alphabets in the string.
Input Format:
- The first line will contain value of string S+

Boundary Conditions:
1 <= Length of S <= 100
Output Format:
The integer value representing the unique count of alphabets in the string S.

Example Input/Output 1:
Input:
level

Output:
3
Explanation:
The unique alphabets are l,e,v. Hence 3 is the output.

Example Input/Output 2:
Input:
manager
Output:
6
print(len(set(input().strip())))
